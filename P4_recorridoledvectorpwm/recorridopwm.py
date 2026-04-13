import RPi.GPIO as GPIO
import time

pines = [17, 27, 22, 10, 9]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pwm_objetos = []
for p in pines:
    GPIO.setup(p, GPIO.OUT)
    pwm = GPIO.PWM(p, 100) 
    pwm.start(0)
    pwm_objetos.append(pwm)

try:
    print("Recorrido Fluido (Sin repeticiones en los extremos)...")
    while True:
        for i in range(len(pwm_objetos)):
            led = pwm_objetos[i]
            max_brillo = 60 if i == 4 else 100
            
            # Subir y bajar rápido para que se vea el movimiento
            for n in range(0, max_brillo + 1, 20):
                led.ChangeDutyCycle(n); time.sleep(0.01)
            for n in range(max_brillo, -1, -20):
                led.ChangeDutyCycle(n); time.sleep(0.01)

        for i in range(len(pwm_objetos) - 2, 0, -1):
            led = pwm_objetos[i]
            for n in range(0, 101, 20):
                led.ChangeDutyCycle(n); time.sleep(0.01)
            for n in range(100, -1, -20):
                led.ChangeDutyCycle(n); time.sleep(0.01)

except KeyboardInterrupt:
    print("\nDetenido")
finally:
    for led in pwm_objetos:
        led.stop()
    GPIO.cleanup()
