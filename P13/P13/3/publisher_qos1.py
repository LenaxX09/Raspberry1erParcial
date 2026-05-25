# publisher_qos1.py
import paho.mqtt.client as mqtt

broker_ip = "10.42.0.117"
topic = "sala/humedad"
mensaje = "Humedad: 60%"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="PubQoS1")

try:
    client.connect(broker_ip, 1883, 60)
    client.loop_start()
    
    # Se captura la información del envío para asegurar el rastreo del ACK
    envio = client.publish(topic, mensaje, qos=1)
    envio.wait_for_publish() # Espera la confirmación PUBACK del Broker
    
    print(f"[QoS 1] Publicado y verificado: {mensaje}")
    
    client.loop_stop()
    client.disconnect()
except Exception as e:
    print(f"Error: {e}")
