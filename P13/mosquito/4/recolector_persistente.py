# recolector_persistente.py
import paho.mqtt.client as mqtt

broker_ip = "10.42.0.117"
topic = "sensores/datos"

def on_message(client, userdata, msg):
    print(f"📥 Mensaje recibido: {msg.payload.decode()} [QoS: {msg.qos}]")

# IMPORTANTE: Para clean_session=False en v2.x se usa la estructura de inicialización limpia
client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2, 
    client_id="RecolectorPersistente", 
    clean_session=False  # Le dice al broker: "Recuerda mi suscripción si me apago"
)
client.on_message = on_message

try:
    print(f"Conectando de forma persistente al broker {broker_ip}...")
    client.connect(broker_ip, 1883, 60)
    
    # Nos suscribimos con QoS 1 (Obligatorio para que funcione la persistencia)
    client.subscribe(topic, qos=1)
    print(f"Suscrito a '{topic}'. Escuchando de forma permanente...")
    
    client.loop_forever()
except KeyboardInterrupt:
    print("\nRecolector detenido.")
finally:
    client.disconnect()
