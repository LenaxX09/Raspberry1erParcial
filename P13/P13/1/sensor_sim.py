# sensor_sim.py
import paho.mqtt.client as mqtt
import time
import random

# CONFIGURACIÓN: Pon la IP real de tu Raspberry Pi
broker = "10.42.0.117" 
topic = "iot/temperatura"

# Inicialización con API v2
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="RaspberryPiPublisher")

try:
    client.connect(broker, 1883, 60)
    print(f"Conectado al broker {broker}. Iniciando transmisión...")
except Exception as e:
    print(f"Error al conectar al broker: {e}")
    exit(1)

client.loop_start()

try:
    while True:
        temperatura = round(random.uniform(20.0, 30.0), 2)
        client.publish(topic, f"{temperatura}")
        print(f"Publicado: {temperatura} °C")
        time.sleep(2)
except KeyboardInterrupt:
    print("\nPublicador detenido")
finally:
    client.loop_stop()
    client.disconnect()
