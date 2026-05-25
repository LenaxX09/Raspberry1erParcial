from sensor import DHT11Sensor
from display import LCDDisplay
from utils import delay

def main():
    sensor = DHT11Sensor()
    lcd = LCDDisplay()
    
    print("Iniciando sistema de monitoreo en LCD...")
    
    while True:
        temp, hum = sensor.read_data()
        
        if temp is not None and hum is not None:
            # Imprime en terminal para que monitorees
            print(f"Datos leídos -> T:{temp:.1f}°C H:{hum:.1f}%")
            # Muestra en la pantalla LCD
            lcd.show_message(f"Temp: {temp:.1f} C", f"Hum: {hum:.1f} %")
        else:
            print("Fallo en lectura, reintentando...")
            lcd.show_message("Sensor", "sin lectura")
            
        delay(2)

if __name__ == "__main__":
    main()
