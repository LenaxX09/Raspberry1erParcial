# P3 - Recorrido LED con Vector

## Descripción
Este proyecto implementa un efecto de movimiento visual usando 5 LEDs que se encienden y apagan secuencialmente de forma alternada (ida y vuelta). Demuestra el uso de vectores/arrays y bucles en programación de sistemas embebidos.

## Objetivo
- Crear un efecto visual de "movimiento" con LEDs
- Aprender a usar vectores/listas para almacenar pines GPIO
- Implementar bucles forward y reverse
- Desarrollar patrones de iluminación dinámicos

## Requisitos de Hardware
- **Raspberry Pi**
- **5 LEDs** de cualquier color
- **5 Resistencias** de 220-330 Ω cada una
- **Jumpers y breadboard**
- **Fuente de alimentación**

## Esquema de Conexión
```
GPIO 17  ----[LED 1]----[Resistencia]---- GND
GPIO 27  ----[LED 2]----[Resistencia]---- GND
GPIO 22  ----[LED 3]----[Resistencia]---- GND
GPIO 10  ----[LED 4]----[Resistencia]---- GND
GPIO 9   ----[LED 5]----[Resistencia]---- GND
```

## Pines GPIO Utilizados
| Posición | GPIO | Pin Físico |
|----------|------|-----------|
| LED 1 | 17 | 11 |
| LED 2 | 27 | 13 |
| LED 3 | 22 | 15 |
| LED 4 | 10 | 19 |
| LED 5 | 9 | 21 |

## Flujo de Ejecución

### Recorrido de IDA
1. LED 1 enciende 0.1s, apaga
2. LED 2 enciende 0.1s, apaga
3. LED 3 enciende 0.1s, apaga
4. LED 4 enciende 0.1s, apaga
5. LED 5 enciende 0.1s, apaga

### Recorrido de VUELTA (reversed)
1. LED 5 enciende 0.1s, apaga
2. LED 4 enciende 0.1s, apaga
3. LED 3 enciende 0.1s, apaga
4. LED 2 enciende 0.1s, apaga
5. LED 1 enciende 0.1s, apaga

Se repite el ciclo indefinidamente

## Componentes del Código

### Vector de Pines
```python
pines = [17, 27, 22, 10, 9]
```

### Configuración Inicial
```python
for pin in pines:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
```

### Recorrido Forward
```python
for pin in pines:
    GPIO.output(pin, GPIO.HIGH)  # Enciende
    time.sleep(0.1)               # Espera 100ms
    GPIO.output(pin, GPIO.LOW)    # Apaga
```

### Recorrido Reverse (usando `reversed()`)
```python
for pin in reversed(pines):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(pin, GPIO.LOW)
```

## Instalación y Uso

### 1. Conectar el circuito
Asegúrate de que todos los LEDs estén correctamente conectados a sus respectivos pines GPIO

### 2. Ejecutar el programa
```bash
sudo python3 recorrido.py
```

### 3. Detener el programa
Presiona **Ctrl+C**

## Resultados Esperados
- Se ve un efecto de movimiento de izquierda a derecha
- Luego se invierte el movimiento (derecha a izquierda)
- Cada LED brilla solo durante 0.1 segundos
- El efecto es fluido y repetitivo

## Variaciones Posibles

### Cambiar velocidad
Modifica `time.sleep(0.1)` a otro valor:
```python
time.sleep(0.05)  # Más rápido
time.sleep(0.2)   # Más lento
```

### Agregar efecto de brillo gradual
Combina con PWM para un efecto más suave (ver Proyecto P4)

### Patrón continuo sin inversión
```python
while True:
    for pin in pines:
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(pin, GPIO.LOW)
```

### Patrón en ambas direcciones simultáneamente
Usar múltiples hilos (threading) para efectos más complejos

## Conceptos Aprendidos
- **Vectores/Listas**: Almacenamiento de múltiples valores
- **Iteración**: Bucles `for` para procesar cada elemento
- **Función `reversed()`**: Invertir el orden de iteración
- **Patrones visuales**: Crear efectos dinámicos con hardware

## Archivos Incluidos
- `recorrido.py`: Script principal del efecto de movimiento
- `P3_recorridoledvector.md`: Documentación completa
- `Pictures/`: Imágenes del setup y circuito

## Notas Importantes
- El delay de 0.1s es suficiente para ver cada LED individualmente
- Si el efecto es muy rápido, aumenta el delay
- Todos los LEDs deben estar correctamente conectados con resistencias
- El orden del vector es importante para el flujo visual

## Siguiente Paso
Progresa al Proyecto P4 para agregar efectos de brillo gradual usando PWM