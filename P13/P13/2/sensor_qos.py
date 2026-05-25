# sensor_qos.py
import paho.mqtt.client as mqtt
import time
import random

# CONFIGURACIÓN: Usando la IP real de tu Raspberry Pi
broker = "10.42.0.117"
topic = "iot/qos/temp"
qos_level = 1  # Cambia entre 0, 1 o 2 para tus experimentos

# Inicialización obligatoria con la API v2 de Paho MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="RaspberryPiQoSPub")

print(f"Intentando conectar al broker Mosquitto en {broker}...")
try:
    client.connect(broker, 1883, 60)
    print("¡Conectado exitosamente!")
except Exception as e:
    print(f"Error al conectar: {e}")
    exit(1)

# Iniciar bucle de red en segundo plano
client.loop_start()

try:
    print(f"Iniciando publicación en el topic '{topic}' con QoS {qos_level}...")
    while True:
        temp = round(random.uniform(20, 30), 2)
        
        # Publicación asíncrona (evita que se congele el script)
        client.publish(topic, f"{temp}", qos=qos_level)
        
        print(f"Publicado con QoS {qos_level}: {temp} °C")
        time.sleep(2)
except KeyboardInterrupt:
    print("\nPublicador detenido")
finally:
    client.loop_stop()
    client.disconnect()
    print("Desconectado correctamente.")
