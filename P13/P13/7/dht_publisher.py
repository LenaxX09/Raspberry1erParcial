# dht_publisher.py
from collections import deque
import board
import adafruit_dht
import paho.mqtt.client as mqtt
import time
import json
from datetime import datetime

GPIO_PIN = board.D17
MQTT_BROKER = "localhost" # Modificar por la IP de la Pi si el broker se mueve
MQTT_PORT = 1883
MQTT_TOPIC = "sensor/dht"
MQTT_QoS = 1
INTERVALO_LECTURA = 5

cola_mensajes = deque()

def leer_dht(sensor, intentos=5, delay=2):
    for intento in range(intentos):
        try:
            t = sensor.temperature
            h = sensor.humidity
            if t is not None and h is not None:
                return t, h
        except RuntimeError as e:
            print(f"[{intento+1}/{intentos}] Reintento de lectura: {e}")
            time.sleep(delay)
    raise RuntimeError("No se pudo obtener una lectura válida del DHT.")

def on_connect(client, userdata, flags, rc, properties=None):
    print("[MQTT] Conectado exitosamente al Broker local.")

def on_publish(client, userdata, mid, *args, **kwargs):
    # Confirmación de llegada al Broker (QoS 1)
    pass

# Inicialización obligatoria con API v2
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="RaspberryPiDHTPub")
client.on_connect = on_connect
client.on_publish = on_publish

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()

# Inicializar sensor (Cambiar a DHT22 si es el modelo que tienes)
dht_sensor = adafruit_dht.DHT11(GPIO_PIN)

print("🚀 Sistema de monitoreo DHT iniciado...")

try:
    while True:
        try:
            temp, hum = leer_dht(dht_sensor)
            timestamp = datetime.now().isoformat()

            mensaje = json.dumps({"timestamp": timestamp, "temperatura": temp, "humedad": hum})
            cola_mensajes.append(mensaje)
            
            # Intentar vaciar la cola local FIFO
            while len(cola_mensajes) > 0:
                actual = cola_mensajes[0]
                result = client.publish(MQTT_TOPIC, actual, qos=MQTT_QoS)
                
                # wait_for_publish asegura que el estado sea verificado antes de avanzar
                result.wait_for_publish()
                
                if result.rc == mqtt.MQTT_ERR_SUCCESS:
                    print(f"📤 Enviado exitosamente de la cola: {actual}")
                    cola_mensajes.popleft() # Quitar solo si se envió
                else:
                    print("⚠️ Falla de envío en red. Conservando datos en RAM...")
                    break

        except Exception as e:
            print("[Error en bucle]:", e)
            
        time.sleep(INTERVALO_LECTURA)

except KeyboardInterrupt:
    print("\n🛑 Publicador finalizado por el usuario.")
finally:
    dht_sensor.exit()
    client.loop_stop()
    client.disconnect()
