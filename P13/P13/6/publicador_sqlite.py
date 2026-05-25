# publicador_sqlite.py
import sqlite3
import time
import random

# Nos conectamos al archivo local (se creará automáticamente si no existe)
conn = sqlite3.connect("mensajes.db")
cursor = conn.cursor()

# Crear la tabla estructurada para la cola FIFO
cursor.execute('''
CREATE TABLE IF NOT EXISTS cola (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mensaje TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()

print("🚀 Publicador de SQLite iniciado. Insertando registros en 'mensajes.db'...")

try:
    while True:
        temp = round(random.uniform(20.0, 30.0), 2)
        mensaje = f"Temperatura: {temp} °C"
        
        # Insertar el mensaje al final de la tabla
        cursor.execute("INSERT INTO cola (mensaje) VALUES (?)", (mensaje,))
        conn.commit()
        
        print(f"📤 Encolado en BD: {mensaje}")
        time.sleep(5)
except KeyboardInterrupt:
    print("\n🛑 Publicador detenido.")
finally:
    conn.close()
