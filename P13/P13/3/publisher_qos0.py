# publisher_qos0.py
import paho.mqtt.client as mqtt

broker_ip = "10.42.0.117"
topic = "sala/temperatura"
mensaje = "Temp: 24.5 °C"

# Inicialización con API v2
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="PubQoS0")

try:
    client.connect(broker_ip, 1883, 60)
    client.loop_start() # Inicia el loop para procesar el envío básico
    
    client.publish(topic, mensaje, qos=0)
    print(f"[QoS 0] Publicado: {mensaje}")
    
    client.loop_stop()
    client.disconnect()
except Exception as e:
    print(f"Error: {e}")
