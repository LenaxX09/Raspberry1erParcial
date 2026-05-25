# subscriptor_sqlite.py
import sqlite3
import time

conn = sqlite3.connect("mensajes.db")
cursor = conn.cursor()

# Asegurar que la tabla exista en caso de que este script se lance primero
cursor.execute('''
CREATE TABLE IF NOT EXISTS cola (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mensaje TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()

print("🕓 Esperando mensajes en mensajes.db (Modo FIFO)...")

try:
    while True:
        # Consultar el registro más antiguo (el ID más bajo)
        cursor.execute("SELECT id, mensaje FROM cola ORDER BY id ASC LIMIT 1")
        fila = cursor.fetchone()
        
        if fila:
            id_msg, mensaje = fila
            print(f"📥 Mensaje consumido: {mensaje} (ID: {id_msg})")
            
            # Remover el mensaje de la tabla para que no se procese de nuevo
            cursor.execute("DELETE FROM cola WHERE id = ?", (id_msg,))
            conn.commit()
        else:
            # Si la tabla está vacía, espera un momento antes de volver a consultar (polling)
            time.sleep(2)
except KeyboardInterrupt:
    print("\n🛑 Subscriptor detenido.")
finally:
    conn.close()
