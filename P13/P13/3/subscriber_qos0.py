# subscriber_qos0.py
import paho.mqtt.client as mqtt

broker_ip = "10.42.0.117"
topic = "sala/temperatura"

def on_message(client, userdata, msg):
    print(f"[QoS 0] Mensaje recibido: {msg.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="SubQoS0")
client.on_message = on_message

try:
    client.connect(broker_ip, 1883, 60)
    client.subscribe(topic, qos=0)
    client.loop_start()

    input("Presiona Enter para salir de QoS 0...\n")
    client.loop_stop()
    client.disconnect()
except Exception as e:
    print(f"Error: {e}")
