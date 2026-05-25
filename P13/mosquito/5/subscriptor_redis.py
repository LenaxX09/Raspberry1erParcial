# subscriptor_redis.py
import redis

# CONFIGURACIÓN: Conexión remota a la IP de la Raspberry Pi
broker_ip = "10.42.0.117"
r = redis.Redis(host=broker_ip, port=6379, db=0)

print(f"🕓 Conectado a Redis en {broker_ip}. Esperando mensajes en modo bloqueante (BLPOP)...")
try:
    while True:
        # BLPOP remueve y devuelve el primer elemento de la lista (Left Pop).
        # Si la lista está vacía, bloquea la ejecución hasta que haya un elemento disponible.
        nombre_cola, mensaje = r.blpop("cola:temperatura")
        
        print(f"📥 Mensaje recibido de [{nombre_cola.decode()}]: {mensaje.decode()}")
except KeyboardInterrupt:
    print("\n🛑 Subscriptor detenido.")
