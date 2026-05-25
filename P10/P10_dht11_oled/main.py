import time
import sys
from sensors.dht11_reader import DHT11Reader
from display.oled_display import OLEDDisplay

def main():
    print("Inicializando Monitor Ambiental...")
    sensor = DHT11Reader()
    display = OLEDDisplay()
    
    print("Monitoreo activo. Leyendo datos...")
    while True:
        temp, hum = sensor.read()
        if temp is not None and hum is not None:
            print(f"[OK] T:{temp}°C H:{hum}%")
            display.update(temp, hum)
        else:
            print("[WARN] Error de sincronía con DHT11, reintentando...")
            
        time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nMonitor ambiental apagado por el usuario.")
        sys.exit(0)
