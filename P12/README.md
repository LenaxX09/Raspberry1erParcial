# P12 - DHT11 Gráfico con Matplotlib

## Descripción
Esta práctica utiliza Matplotlib para crear gráficos más sofisticados y detallados del sensor DHT11, permitiendo análisis visual de datos históricos.

## Objetivos
- Utilizar Matplotlib para visualización avanzada
- Crear gráficos de temperatura y humedad
- Guardar y mostrar datos históricos
- Realizar análisis visual de tendencias

## Requisitos
- Raspberry Pi
- Python con Matplotlib instalado
- Sensor DHT11
- Librerías de base de datos (opcional)

## Contenido
- **P12 - DHT11 Graph via Matplotlib.odt**: Documentación
- **P12_dht11_lab/**: Código con ejemplos

## Características
1. **Gráficos en tiempo real**: Actualización continua
2. **Gráficos guardados**: Exportación a PNG/PDF
3. **Análisis estadístico**: Media, máximo, mínimo
4. **Múltiples ejes**: Temperatura y humedad simultáneamente

## Ejemplo de Gráfico
```python
import matplotlib.pyplot as plt
plt.plot(tiempo, temperatura, label='Temperatura')
plt.plot(tiempo, humedad, label='Humedad')
plt.legend()
plt.show()
```

## Almacenamiento de Datos
- Archivos CSV para datos históricos
- Base de datos SQLite (opcional)
- Sincronización periódica
