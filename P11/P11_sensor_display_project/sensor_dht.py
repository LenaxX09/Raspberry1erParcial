import adafruit_dht
from config import DHT_PIN

class SensorDHT:
    def __init__(self, pin=DHT_PIN):
        # CORRECCIÓN: Desactivamos pulseio para evitar el congelamiento en 64 bits
        self.dht = adafruit_dht.DHT11(pin, use_pulseio=False)

    def leer(self):
        try:
            temp = self.dht.temperature
            hum = self.dht.humidity
            if temp is not None and hum is not None:
                return temp, hum
            else:
                raise ValueError("Lectura inválida del sensor.")
        except RuntimeError as e:
            # Los DHT11 fallan mucho por tiempo, si avisa ruido, lo ignoramos y reintenta solo
            print("Aviso de lectura DHT11 (reintentando):", e.args[0])
            return None, None

    def cerrar(self):
        self.dht.exit()
