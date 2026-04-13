# P2 - Semáforo con Control Horario

## Descripción
Este proyecto implementa un semáforo controlado por una Raspberry Pi que opera según un horario escolar específico. El semáforo solo funciona entre las 5:00 AM y las 9:59 PM, simulando un horario de operación realista.

## Objetivo
- Controlar tres LEDs (rojo, amarillo, verde) que simulan un semáforo
- Implementar control horario basado en la hora del sistema
- Agregar efectos de parpadeo al LED verde
- Aprender sobre variables y estructuras de control condicional

## Requisitos de Hardware
- **Raspberry Pi** con reloj del sistema configurado
- **3 LEDs** (rojo, amarillo, verde)
- **3 Resistencias** de 220-330 Ω cada una
- **Jumpers y breadboard**
- **Fuente de alimentación**

## Esquema de Conexión
```
GPIO 17 (Rojo)     ----[LED Rojo]----[Resistencia]---- GND
GPIO 27 (Amarillo) ----[LED Amarillo]----[Resistencia]---- GND
GPIO 22 (Verde)    ----[LED Verde]----[Resistencia]---- GND
```

## Pines GPIO Utilizados
| Color | GPIO | Pin Físico |
|-------|------|-----------|
| Rojo | 17 | 11 |
| Amarillo | 27 | 13 |
| Verde | 22 | 15 |

## Secuencia del Semáforo

### Horario Activo (5:00 AM - 9:59 PM)
1. **Verde**: 5 segundos
2. **Verde Parpadeante**: 3 parpadeos (0.5s encendido/apagado)
3. **Amarillo**: 2 segundos
4. **Rojo**: 5 segundos
5. Se repite el ciclo

### Horario Nocturno (10:00 PM - 4:59 AM)
- Todos los LEDs apagados
- Verifica cada minuto si ha comenzado el horario escolar

## Componentes del Código

### Variables Principales
```python
ROJO, AMARILLO, VERDE = 17, 27, 22
```

### Función Auxiliar
- **apagar_todo()**: Apaga todos los LEDs simultáneamente

### Control Horario
```python
ahora = datetime.now().hour
if 5 <= ahora < 22:  # Horario activo
```

## Instalación y Uso

### 1. Verificar la hora del sistema
```bash
timedatectl status
```

### 2. Ejecutar el programa
```bash
sudo python3 semaforo.py
```

### 3. Detener el programa
Presiona **Ctrl+C**

## Resultados Esperados
- **De día (5:00-21:59)**: El semáforo cicla continuamente con los colores RGB
- **De noche (22:00-04:59)**: Los LEDs están apagados
- **Mensajes en consola**: Muestran la hora y el estado actual del semáforo

## Mejoras Futuras
- Integrar con sensores de movimiento o tráfico
- Usar una RTC (Real Time Clock) externa para mayor precisión
- Agregar botones para control manual
- Implementar diferentes patrones según el día de la semana

## Archivos Incluidos
- `semaforo.py`: Script principal del semáforo inteligente
- `P2_semaforoleds.md`: Documentación detallada
- `Pictures/`: Imágenes del circuito

## Conceptos Aprendidos
- Control de múltiples GPIO simultáneamente
- Importación de módulos (`datetime`)
- Estructuras condicionales complejas
- Uso de bucles y delays temporales
- Efectos de parpadeo mediante software

## Notas Importantes
- Asegúrate de que la hora del sistema sea correcta
- La precisión del control horario depende del reloj del sistema
- Si experimentas problemas, reinicia la Raspberry Pi para sincronizar la hora
