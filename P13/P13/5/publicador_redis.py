import redis
import time
import random

# Conexión al Redis local de la Raspberry Pi
r = redis.Redis(host='localhost', port=6379, db=0)

print("🚀 Productor de Redis iniciado. Insertando datos en la cola...")
try:
    while True:
        temp = round(random.uniform(20.0, 30.0), 2)
        mensaje = f"Temperatura: {temp} °C"
        
        # Inserta el mensaje al final de la lista (Right Push)
        r.rpush("cola:temperatura", mensaje)
        
        print("📤 Encolado exitosamente:", mensaje)
        time.sleep(5)
except KeyboardInterrupt:
    print("\n🛑 Publicador detenido.")
