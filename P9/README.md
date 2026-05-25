# P9 - Display OLED con Desplazamiento

## Descripción
Esta práctica implementa efectos de desplazamiento y animaciones en pantallas OLED para crear interfaces más dinámicas.

## Objetivos
- Implementar scroll en pantallas OLED
- Crear animaciones gráficas
- Optimizar el rendimiento gráfico
- Desarrollar interfaces más complejas

## Requisitos
- Raspberry Pi
- Pantalla OLED (128x64)
- Librerías PIL y Adafruit OLED
- Conocimientos de gráficos de píxeles

## Contenido
- **P9-OLED-Scroll.odt**: Documentación de técnicas de scroll
- **P9_oled_scrolling/**: Código implementado

## Técnicas Implementadas
1. **Scroll de texto**: Movimiento suave de caracteres
2. **Scroll de imágenes**: Desplazamiento de gráficos
3. **Animaciones**: Cambios de frame continuos

## Optimizaciones
- Buffer de pantalla para actualización eficiente
- Control de velocidad de fotogramas (FPS)
- Manejo de memoria para imágenes grandes

## Ejemplo de Animación
```python
for frame in range(num_frames):
    dibujar_frame(frame)
    oled.display()
    tiempo.sleep(1/30)  # 30 FPS
```
