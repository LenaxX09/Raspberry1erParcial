# sensor_persistente.py
import paho.mqtt.client as mqtt
from queue import Queue
import time
import random

broker = "10.42.0.117"  # IP de tu Raspberry Pi
topic = "sensores/datos"

# Cola en memoria RAM para almacenar datos si se cae la red
mensaje_queue = Queue()

# Usamos la API v2 de Paho
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="PublicadorPersistente")

def on_connect(client, userdata, flags, rc, properties=None):
    print("¡Conectado exitosamente al broker!")
    # Al reconectarse, vacía la cola local enviando los datos acumulados
    while not mensaje_queue.empty():
        mensaje_pendiente = mensaje_queue.get()
        client.publish(topic, mensaje_pendiente, qos=1)
        print(f"📦 Enviado desde la cola local: {mensaje_pendiente}")

def on_disconnect(client, userdata, disconnect_flags, rc, properties=None):
    print("🔴 Desconectado del broker. Activando almacenamiento local...")

client.on_connect = on_connect
client.on_disconnect = on_disconnect

# Conexión asíncrona para que no bloquee el script principal si el broker se cae
client.connect_async(broker, 1883, 60)
client.loop_start()

try:
    while True:
        temp = round(random.uniform(20, 30), 2)
        mensaje = f"Temp: {temp} °C"
        
        # Verificar si el cliente de red está activo
        if client.is_connected():
            client.publish(topic, mensaje, qos=1)
            print(f"🚀 Publicado en tiempo real: {mensaje}")
        else:
            # Si la red está caída, se guarda en la memoria interna de la Pi
            mensaje_queue.put(mensaje)
            print(f"⚠️ Red caída. Guardado en cola local (Total: {mensaje_queue.qsize()}): {mensaje}")
            
        time.sleep(2)
except KeyboardInterrupt:
    print("\nPublicador finalizado.")
finally:
    client.loop_stop()
    client.disconnect()
