import time
import board                                 # <-- ¡ESTE IMPORT ES CLAVE!
from sensor_reader import DHT11Reader
from plotter import LivePlotter

def main():
    # Forzamos al lector a usar el GPIO 17 en lugar del 4 por defecto
    sensor = DHT11Reader(board.D17)          # <-- SE CAMBIÓ AQUÍ
    plotter = LivePlotter()
    start_time = time.time()
    
    print("Iniciando lectura... Presiona Ctrl+C para detener.")
    
    try:
        while True:
            data = sensor.read()
            elapsed_time = round(time.time() - start_time, 1)
            
            if data:
                temperature, humidity = data
                print(f"[{elapsed_time}s] Temp: {temperature}°C | Humedad: {humidity}%")
                plotter.update(elapsed_time, temperature, humidity)
            else:
                print(f"[{elapsed_time}s] Alerta: Lectura del sensor omitida (ruido de bus).")
            
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n[INFO] Lectura finalizada por el usuario.")
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        plotter.cerrar()
        print("[INFO] Cerrando aplicación.")

if __name__ == "__main__":
    main()
