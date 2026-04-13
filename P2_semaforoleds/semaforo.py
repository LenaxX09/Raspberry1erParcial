import RPi.GPIO as GPIO
import time
from datetime import datetime  # Para revisar la hora del sistema

ROJO, AMARILLO, VERDE = 17, 27, 22

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup([ROJO, AMARILLO, VERDE], GPIO.OUT, initial=GPIO.LOW)

def apagar_todo():
    GPIO.output([ROJO, AMARILLO, VERDE], GPIO.LOW)

try:
    print("--- Semáforo con Horario Escolar (TESOEM) ---")
    while True:
        # 1. Obtener la hora actual
        ahora = datetime.now().hour
        
        # 2. Verificar condición: Funciona de 5:00 AM a 9:59 PM (22 hrs)
        if 5 <= ahora < 22:

            print(f"[{datetime.now().strftime('%H:%M:%S')}] SEMÁFORO ACTIVO")
            
            GPIO.output(VERDE, GPIO.HIGH)
            print("VERDE")
            time.sleep(5)
            
            # Parpadeo verde
            for _ in range(3):
                GPIO.output(VERDE, GPIO.LOW); time.sleep(0.5)
                GPIO.output(VERDE, GPIO.HIGH); time.sleep(0.5)
            GPIO.output(VERDE, GPIO.LOW)

            GPIO.output(AMARILLO, GPIO.HIGH)
            print("AMARILLO")
            time.sleep(2)
            GPIO.output(AMARILLO, GPIO.LOW)

            GPIO.output(ROJO, GPIO.HIGH)
            print("ROJO")
            time.sleep(5)
            GPIO.output(ROJO, GPIO.LOW)
        else:
            # --- FUERA DE SERVICIO (22:00 a 04:59) ---
            print(f"[{datetime.now().strftime('%H:%M:%S')}] FUERA DE OPERACIÓN (Horario nocturno)")
            apagar_todo()
            time.sleep(60) # Revisa cada minuto si ya son las 5 AM

except KeyboardInterrupt:
    print("\nPrograma detenido")
finally:
    GPIO.cleanup()
