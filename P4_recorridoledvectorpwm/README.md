# P4 - Recorrido LED con PWM y Transiciones Fluidas

## Descripción
Este proyecto avanza sobre P3 agregando control de brillo usando PWM (Modulación por Ancho de Pulso). Crea un efecto visual suave y fluido donde los LEDs aumentan y disminuyen gradualmente su intensidad, simulando un movimiento más realista.

## Objetivo
- Dominar PWM (Pulse Width Modulation) para control de brillo
- Crear transiciones suaves de iluminación
- Implementar recorridos fluidos sin repeticiones en los extremos
- Aprender técnicas avanzadas de control GPIO

## Requisitos de Hardware
- **Raspberry Pi**
- **5 LEDs** (preferiblemente del mismo color para mejor efecto)
- **5 Resistencias** de 220-330 Ω cada una
- **Jumpers y breadboard**
- **Fuente de alimentación estable**

## Esquema de Conexión
```
GPIO 17  ----[LED 1]----[Resistencia]---- GND
GPIO 27  ----[LED 2]----[Resistencia]---- GND
GPIO 22  ----[LED 3]----[Resistencia]---- GND
GPIO 10  ----[LED 4]----[Resistencia]---- GND
GPIO 9   ----[LED 5]----[Resistencia]---- GND
```

## Pines GPIO Utilizados
| Posición | GPIO | Pin Físico | Frecuencia PWM |
|----------|------|-----------|----------------|
| LED 1 | 17 | 11 | 100 Hz |
| LED 2 | 27 | 13 | 100 Hz |
| LED 3 | 22 | 15 | 100 Hz |
| LED 4 | 10 | 19 | 100 Hz |
| LED 5 | 9 | 21 | 100 Hz |

## Componentes del Código

### Configuración PWM
```python
pwm_objetos = []
for p in pines:
    GPIO.setup(p, GPIO.OUT)
    pwm = GPIO.PWM(p, 100)    # 100 Hz de frecuencia
    pwm.start(0)              # Comienza en 0% duty cycle
    pwm_objetos.append(pwm)
```

### Control de Brillo
```python
led.ChangeDutyCycle(valor)  # valor: 0-100
# 0 = apagado, 100 = máximo brillo
```

### Parámetros Especiales
- **LED 5 (último)**: Brillo máximo de 60% en lugar de 100%
- **Incremento de brillo**: De 20 en 20 (20%, 40%, 60%, 80%, 100%)
- **Delay entre cambios**: 0.01 segundos para transición suave

## Flujo de Ejecución

### Primera Etapa - Recorrido Forward
1. LED 1: Sube 0→100%, baja 100→0%
2. LED 2: Sube 0→100%, baja 100→0%
3. LED 3: Sube 0→100%, baja 100→0%
4. LED 4: Sube 0→100%, baja 100→0%
5. LED 5: Sube 0→60%, baja 60→0% (brillo limitado)

### Segunda Etapa - Recorrido Reverse (sin extremos)
1. LED 4: Sube 0→100%, baja 100→0%
2. LED 3: Sube 0→100%, baja 100→0%
3. LED 2: Sube 0→100%, baja 100→0%
4. (LED 5 y LED 1 se omiten en vuelta para efecto continuo)

Se repite indefinidamente

## Instalación y Uso

### 1. Verificar soporte PWM
Los pines GPIO 17, 27, 22, 10, 9 soportan software PWM

### 2. Ejecutar el programa
```bash
sudo python3 recorridopwm.py
```

### 3. Detener el programa
Presiona **Ctrl+C**

## Resultados Esperados
- **Efecto fluido**: Los LEDs aumentan y disminuyen suavemente el brillo
- **Movimiento continuo**: Se ve como una onda de luz recorriendo los LEDs
- **Sin titiriteo**: El cambio es suave gracias a los pequeños incrementos (20%)
- **Duración del ciclo**: Aproximadamente 2 segundos por recorrido completo

## Conceptos PWM Explicados

### Duty Cycle
- **0%**: LED apagado
- **25%**: LED a 25% del brillo máximo
- **50%**: LED a 50% del brillo máximo
- **100%**: LED a máximo brillo

### Frecuencia
- **100 Hz**: 100 ciclos por segundo
- Suficiente para que el ojo humano no perciba titiriteo
- Mayor frecuencia = transiciones más suaves

## Variaciones Posibles

### Aumentar velocidad
Cambiar `time.sleep(0.01)` a valor menor:
```python
time.sleep(0.005)  # El doble de rápido
```

### Efecto de respiración
```python
while True:
    for duty in range(0, 101, 5):
        pwm.ChangeDutyCycle(duty)
        time.sleep(0.05)
    for duty in range(100, -1, -5):
        pwm.ChangeDutyCycle(duty)
        time.sleep(0.05)
```

### Rainbow effect (arco iris)
Controlar múltiples LEDs simultáneamente con diferentes patrones

### Onda continua sin interrupciones
Usar funciones trigonométricas para cálculos más complejos

## Comparativa: Digital vs PWM

| Característica | P3 Digital | P4 PWM |
|---|---|---|
| Estados LED | Solo encendido/apagado | 101 niveles de brillo |
| Suavidad | Abrupta | Fluida |
| Velocidad | Rápida | Más lenta (por cálculos) |
| Efecto visual | Saltos | Transiciones graduales |

## Archivos Incluidos
- `recorridopwm.py`: Script principal con PWM avanzado
- `P4_recorridoledvectorpwm.md`: Documentación técnica completa
- `Pictures/`: Imágenes del circuito y videos del efecto

## Conceptos Aprendidos
- **PWM (Modulación por Ancho de Pulso)**: Control de potencia analógica
- **Duty Cycle**: Porcentaje de tiempo en estado alto
- **Frecuencia**: Ciclos por segundo
- **Transiciones suaves**: Incrementos pequeños para fluidez
- **Objetos en Python**: Almacenar múltiples instancias PWM
- **Control fino de hardware**: Más allá de encendido/apagado

## Troubleshooting

### LED titila en lugar de suavidad
- Aumenta la frecuencia PWM (mayor a 100 Hz)
- Reduce el valor de `time.sleep()` entre cambios

### LEDs no responden a PWM
- Verifica que los pines soporte software PWM
- Comprueba el cableado
- Asegúrate de usar `GPIO.PWM()` correctamente

### Efecto muy lento
- Reduce `time.sleep(0.01)` a un valor menor
- Aumenta el incremento de duty cycle (de 20 en 20 a 25 o 30)

## Notas Importantes
- PWM por software puede ser menos eficiente que hardware PWM
- La Raspberry Pi es capaz de ejecutar múltiples PWM simultáneamente
- Para aplicaciones críticas, considera usar hardware PWM dedicado
- Siempre utiliza resistencias apropiadas para proteger los LEDs

## Siguiente Paso
Combina estos proyectos con sensores (ultrasónicos, infrarrojos, distancia) para crear sistemas interactivos