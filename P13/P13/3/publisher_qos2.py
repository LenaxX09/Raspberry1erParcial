# publisher_qos2.py
import paho.mqtt.client as mqtt

broker_ip = "10.42.0.117"
topic = "sala/gas"
mensaje = "Alerta: Nivel de gas elevado"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="PubQoS2")

try:
    client.connect(broker_ip, 1883, 60)
    client.loop_start()
    
    # Inicia el handshake de 4 pasos por red
    envio = client.publish(topic, mensaje, qos=2)
    envio.wait_for_publish() # Espera hasta completar el ciclo completo (PUBCOMP)
    
    print(f"[QoS 2] Publicado con Handshake de 4 pasos completo: {mensaje}")
    
    client.loop_stop()
    client.disconnect()
except Exception as e:
    print(f"Error: {e}")
