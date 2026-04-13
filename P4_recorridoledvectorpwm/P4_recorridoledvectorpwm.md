![](Pictures/100000000000012C0000005AEAF22963.png){width="4.939cm"
height="1.446cm"}![](Pictures/10000000000001900000019068EC48D7.png){width="3.279cm"
height="3.279cm"}

**Práctica 4 Recorrido de Leds Vector PWM**

**Nombre del docente:**\
Gustavo Moises Romero Gonzalez

**Materia:**

Sistemas Embebidos Aplicados a Móviles**\
**

**Nombre del alumno(a):**

\
Cabañas Santamaria Anel Athziri\
Miranda Martinez Alejandro\
Roldan Velazquez Ian Jurguen

Desarrollo de la Práctica

¿Qué se hará? Se realizara un proceso de recorrido LED, controlado
mediante un programa Python que emplee el uso de un vector de control
GPIO con un brevev ajuste que es mejorar el programa usando controles
PWM para controlar el brillo de los LEDS.

1\. Creación de carpeta y archivo.

![](Pictures/1000000100000500000002FF1B5E7F4C.png){width="21.091cm"
height="2.385cm"}\
Se creó un directorio dentro de proyectos para organizar el proyecto y
se utilizó el editor de texto *nano* para escribir el script en Python.\
\
\
***Adjunto Programa:\
***

import RPi.GPIO as GPIO

import time

pines = \[17, 27, 22, 10, 9\]

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

pwm_objetos = \[\]

for p in pines:

GPIO.setup(p, GPIO.OUT)

pwm = GPIO.PWM(p, 100)

pwm.start(0)

pwm_objetos.append(pwm)

try:

print(\"Recorrido Fluido (Sin repeticiones en los extremos)\...\")

while True:

for i in range(len(pwm_objetos)):

led = pwm_objetos\[i\]

max_brillo = 60 if i == 4 else 100

\# Subir y bajar rápido para que se vea el movimiento

for n in range(0, max_brillo + 1, 20):

led.ChangeDutyCycle(n); time.sleep(0.01)

for n in range(max_brillo, -1, -20):

led.ChangeDutyCycle(n); time.sleep(0.01)

for i in range(len(pwm_objetos) - 2, 0, -1):

led = pwm_objetos\[i\]

for n in range(0, 101, 20):

led.ChangeDutyCycle(n); time.sleep(0.01)

for n in range(100, -1, -20):

led.ChangeDutyCycle(n); time.sleep(0.01)

except KeyboardInterrupt:

print(\"\\nDetenido\")

finally:

for led in pwm_objetos:

led.stop()

GPIO.cleanup()

\
**2. Instalación de la librería.**

![](Pictures/100000000000023A00000057DEA0D5A2.png){width="18.336cm"
height="2.798cm"}\
Al ejecutar el código nos dará este anuncio como la ves anterior por eso
se debe tener instalado la librería dentro de esa carpeta.\
\
Hacemos uso del comando pip install Rpi.GPIO como se ve aquí:\
![](Pictures/10000000000003570000007CFAE41A7A.png){width="21.02cm"
height="3.048cm"}\
\
\
\
\
\
\
\
\
\
\
\
**3. Ejecución de programa y implementarlo en protoboard.\
**Una vez resueltas las dependencias, se ejecutó el programa
exitosamente, observando que el programa lo hace en el protoboard:\
![](Pictures/10000000000002C20000003C80564961.png){width="19.59cm"
height="1.663cm"}

Asi de debe estar imlementado en el protoboard, ocuparemos 5 leds,
Jumpers (HEMBRA-MACHO), 5 resistencias de 220 ohms, un protoboard y el
Raspberry pi.

Ocuparemos del Raspberry Pi 4 los siguientes pines:\
\
Pin Físico 11: Corresponde al GPIO 17. Es el pin encargado de enviar la
señal de 3.3V para encender el LED Rojo.

Pin Físico 13: Corresponde al GPIO 27. Es el pin encargado de enviar la
señal de 3.3V para encender el LED Amarillo.

Pin Físico 15: Corresponde al GPIO 22. Es el pin encargado de enviar la
señal de 3.3V para encender el LED Azul.

Pin Físico 19: Corresponde al GPIO 10. Es el pin encargado de enviar la
señal de 3.3V para encender el LED Verde.

Pin Físico 21: Corresponde al GPIO 9. Es el pin encargado de enviar la
señal de 3.3V para encender el LED Azul.

![](Pictures/10000000000004000000024C6A7798AC.png){width="17.59cm"
height="10.1cm"}Pin Físico 6: Corresponde a Ground (GND). Es el punto de
retorno de la corriente para cerrar el circuito.\
\
La conexión al protoboard es: los pines 11, 13, 15, 19 y 21 con el
jumper sera conectado a cada LED, lo siguiente es conectarle la
resistencia de 220 ohms del negativo al cátodo de cada LED y conectar el
pin 6 al lado negativo.\
\
\

Aquí muestro el funcionamiento de la practica:

![](Pictures/1000000000000C0000000FF0320F2587.jpg){width="17.59cm"
height="23.361cm"}

***\
***![](Pictures/1000000000000C0000000FF0BB283EBB.jpg){width="17.59cm"
height="23.361cm"}***\
\
\
\
\
\
***![](Pictures/1000000000000FF000000C000C5B1514.jpg){width="17.59cm"
height="13.243cm"}***\
\
\
\
\
\
\
\
\
\
***![](Pictures/1000000000000FF000000C00DEBE0F56.jpg){width="17.59cm"
height="13.243cm"}***\
\
\
\
\
\
\
\
\
\
\
\
\
\
***

***\
\
\
\
\
Conclusión:***\
Se aplicó la técnica de Modulación por Ancho de Pulso (PWM) para
transformar señales digitales en salidas con intensidad variable. A
través de la manipulación del ciclo de trabajo (Duty Cycle), se logró un
efecto de desvanecimiento (fading) en el recorrido de los LEDs.
Asimismo, el uso de PWM permitió compensar mediante software las
diferencias de brillo causadas por el uso de distintos valores de
resistencias (100, 220 y 300), logrando una iluminación uniforme en todo
el sistema.
