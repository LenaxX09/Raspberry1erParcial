# P11 - OLED con Gráficos

## Descripción
Esta práctica implementa la visualización de datos en forma de gráficos en pantallas OLED, permitiendo visualizar tendencias y patrones en tiempo real.

## Objetivos
- Crear gráficos dinámicos en OLED
- Visualizar datos del sensor DHT11 en forma gráfica
- Implementar histogramas y líneas de tendencia
- Optimizar la actualización de gráficos

## Requisitos
- Raspberry Pi
- Pantalla OLED (128x64)
- Sensor DHT11
- Librerías matplotlib o gráficas personalizadas

## Contenido
- **P11-OLED-Grafico.odt**: Documentación de gráficos
- **P11_sensor_display_project/**: Proyecto con gráficos

## Tipos de Gráficos Implementados
1. **Gráfico de línea**: Tendencia de temperatura/humedad
2. **Histograma**: Distribución de valores
3. **Indicadores**: Barras de progreso

## Algoritmo de Gráfico de Línea
```python
# Normalizar datos a escala de pantalla
# Dibujar puntos y conectar con líneas
# Desplazar gráfico con nuevos datos
```

## Rendimiento
- Actualización a 1 FPS típicamente
- Almacenamiento de últimos 100 puntos
- Escalado automático de ejes
