# P7 - LCD con Desplazamiento

## Descripción
Esta práctica amplía los conocimientos de pantallas LCD implementando efectos de desplazamiento de texto (scrolling) para mostrar mensajes más largos que el ancho de la pantalla.

## Objetivos
- Implementar algoritmos de desplazamiento de texto
- Controlar la velocidad y dirección del scroll
- Crear efectos visuales atractivos
- Optimizar el uso del espacio en pantalla

## Requisitos
- Raspberry Pi
- Pantalla LCD (16x2)
- Librerías de control LCD

## Contenido
- **P7-LCD-Scrolling.odt**: Documentación con ejemplos de scroll
- **P7_lcd_scroll/**: Implementación del código de desplazamiento

## Tipos de Desplazamiento
1. **Scroll horizontal**: Movimiento de izquierda a derecha
2. **Scroll vertical**: Movimiento entre líneas
3. **Bounce**: Desplazamiento con rebote en extremos

## Implementación Básica
```python
# Desplazamiento de texto de derecha a izquierda
for i in range(len(texto)):
    pantalla.mostrar(texto[i:])
    tiempo.sleep(0.3)
```

## Parámetros Configurables
- Velocidad de desplazamiento
- Dirección (izq/der, arriba/abajo)
- Efecto de pausa en extremos
