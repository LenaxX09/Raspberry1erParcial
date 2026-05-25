import time
from config import REFRESH_DELAY, HIST_MAX_POINTS
from sensor_dht import SensorDHT
from oled_visualizer import OledVisualizer

def main():
    print("Inicializando Monitor Ambiental Avanzado...")
    
    # Instancia el procesador gráfico (abre la conexión I2C automáticamente)
    visual = OledVisualizer()
    
    # Conecta con el sensor físico DHT
    sensor = SensorDHT()

    # Estructuras de datos dinámicas para emular un comportamiento de buffer FIFO
    temp_hist = []
    hum_hist = []

    print("Monitoreo activo. Graficando datos en tiempo real...")
    print("Presiona Ctrl + C para finalizar el programa de forma segura.\n")

    try:
        while True:
            # Extracción de métricas desde el sensor
            temp, hum = sensor.leer()
            
            if temp is not None and hum is not None:
                print(f"[OK] Muestra registrada -> Temp: {temp:.1f}°C | Hum: {hum:.1f}%")
                
                temp_hist.append(temp)
                hum_hist.append(hum)

                if len(temp_hist) > HIST_MAX_POINTS:
                    temp_hist.pop(0)
                if len(hum_hist) > HIST_MAX_POINTS:    # Bug 3 corregido
                    hum_hist.pop(0)

                # Si las listas alcanzan el límite horizontal de píxeles, descartan el bit más viejo
                if len(temp_hist) > HIST_MAX_POINTS:
                    temp_hist.pop(0)
                    hum_hist.pop(0)

                # Actualiza el lienzo y lo envía a la pantalla
                visual.mostrar_datos(temp, hum, temp_hist, hum_hist)
            else:
                print("[WARN] Lectura ruidosa detectada. Saltando actualización de pantalla...")

            # Pausa controlada para no saturar el protocolo I2C
            time.sleep(REFRESH_DELAY)

    except KeyboardInterrupt:
        print("\n[INFO] Ejecución interrumpida de forma voluntaria por el usuario.")

    except Exception as e:
        print(f"\n[ERROR] Ocurrió una anomalía inesperada en el sistema: {e}")

    finally:
        # Clausura del hilo y liberación de pines GPIO de la Raspberry Pi
        print("[INFO] Liberando recursos de hardware y cerrando conexión con DHT11...")
        sensor.cerrar()
        print("[INFO] Sistema apagado correctamente.")

if __name__ == "__main__":
    main()
