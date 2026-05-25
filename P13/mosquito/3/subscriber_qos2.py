# subscriber_qos2.py
import paho.mqtt.client as mqtt

broker_ip = "10.42.0.117"
topic = "sala/gas"

def on_message(client, userdata, msg):
    print(f"[QoS 2] Mensaje recibido de forma exacta: {msg.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="SubQoS2")
client.on_message = on_message

try:
    client.connect(broker_ip, 1883, 60)
    client.subscribe(topic, qos=2)
    client.loop_start()

    input("Presiona Enter para salir de QoS 2...\n")
    client.loop_stop()
    client.disconnect()
except Exception as e:
    print(f"Error: {e}")
