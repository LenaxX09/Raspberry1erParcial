# P1 - Control de LED Parpadeo

## Descripción
Este proyecto implementa un control simple de un LED en una Raspberry Pi que parpadea de forma continua. Es el primer paso para aprender a controlar componentes GPIO en una Raspberry Pi.

## Objetivo
- Configurar un LED en el GPIO 18 (Pin físico 12)
- Encender y apagar el LED en intervalos de 1 segundo
- Aprender los conceptos básicos de control GPIO

## Requisitos de Hardware
- **Raspberry Pi** (cualquier modelo)
- **LED rojo** (o del color que prefieras)
- **Resistencia** de 220-330 Ω
- **Jumpers y breadboard** (opcional)
- **Fuente de alimentación** para la Raspberry Pi

## Esquema de Conexión
```
GPIO 18 (Pin 12) ----[LED]----[Resistencia]---- GND (Pin 6 o 9)
```

## Componentes del Código
### Configuración Inicial
- **GPIO.setmode(GPIO.BCM)**: Usa la numeración BCM para los pines
- **GPIO.setwarnings(False)**: Desactiva advertencias (opcional)
- **GPIO.setup(LED_PIN, GPIO.OUT)**: Configura el pin 18 como salida

### Loop Principal
- **GPIO.output(LED_PIN, GPIO.HIGH)**: Enciende el LED (3.3V)
- **time.sleep(1)**: Espera 1 segundo
- **GPIO.output(LED_PIN, GPIO.LOW)**: Apaga el LED (0V)

### Limpieza
- **GPIO.cleanup()**: Restaura los pines a su estado inicial

## Instalación y Uso

### 1. Instalar la librería RPi.GPIO
```bash
sudo apt-get install python3-rpi.gpio
```

### 2. Ejecutar el programa
```bash
sudo python3 blink.py
```

### 3. Detener el programa
Presiona **Ctrl+C** para interrumpir la ejecución

## Resultados Esperados
- El LED parpadea continuamente
- Cada ciclo dura 2 segundos (1 segundo encendido + 1 segundo apagado)
- Los mensajes en la consola indican el estado del LED

## Variaciones Posibles
- Cambiar el tiempo de espera en `time.sleep()` para parpadeos más rápidos o lentos
- Usar múltiples LEDs simultáneamente
- Controlar la intensidad con PWM (Proyecto P4)

## Archivos Incluidos
- `blink.py`: Script principal de control del LED
- `P1_ledblink.md`: Documentación detallada del proyecto
- `Pictures/`: Imágenes del circuito y setup

## Notas Importantes
- Requiere permisos de administrador (`sudo`) para acceder a GPIO
- Siempre usa resistencias para proteger los LEDs
- No conectes directamente el LED al GPIO sin resistencia