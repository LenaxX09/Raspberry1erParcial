import RPi.GPIO as GPIO
import time

pines = [17, 27, 22, 10, 9]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for pin in pines:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

try:
    print("Ejecutando Recorrido Digital (Vector)...")
    print("Presiona Ctrl+C para detener")
    
    while True:
        # Recorrido de IDA
        for pin in pines:
            GPIO.output(pin, GPIO.HIGH) # Enciende
            time.sleep(0.1)             # Espera
            GPIO.output(pin, GPIO.LOW)  # Apaga
            
        # Recorrido de VUELTA (usando la función reversed)
        for pin in reversed(pines):
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(pin, GPIO.LOW)

except KeyboardInterrupt:
    print("\nPrograma detenido por el usuario.")
finally:
    GPIO.cleanup()
    print("GPIO liberado correctamente.")
