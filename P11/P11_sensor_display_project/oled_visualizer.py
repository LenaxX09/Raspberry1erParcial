from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from luma.core.render import canvas
from PIL import Image, ImageDraw, ImageFont
from config import *
from utils import escalar

class OledVisualizer:
    def __init__(self, width=OLED_WIDTH, height=OLED_HEIGHT,
                 icon_temp_path=ICON_TEMP_PATH, icon_hum_path=ICON_HUM_PATH):
        self.width = width
        self.height = height
        self.serial = i2c(port=1, address=I2C_ADDRESS)
        self.display = sh1106(self.serial, width=width, height=height, rotate=0)
        self.font = ImageFont.load_default()
        self.icon_temp = Image.open(icon_temp_path).convert("1")
        self.icon_hum = Image.open(icon_hum_path).convert("1")
        self.anim_offset = 0
        self.anim_dir = 1

    def actualizar_animacion(self):
        self.anim_offset += self.anim_dir
        if abs(self.anim_offset) >= ANIM_LIMIT:
            self.anim_dir *= -1

    def mostrar_datos(self, temp, hum, temp_hist, hum_hist):
        self.actualizar_animacion()

        # luma.canvas maneja internamente el buffer, el offset de 132 col y la conversion de bits
        with canvas(self.display) as draw:
            # El fondo ya es negro por defecto dentro del canvas de luma

            # Iconos animados — paste directo sobre la imagen interna del canvas
            draw._image.paste(self.icon_temp, (0, 0 + self.anim_offset))
            draw._image.paste(self.icon_hum, (0, self.height - 16 - self.anim_offset))

            # Texto de valores
            draw.text((20, 0), f"{temp:.1f} C", font=self.font, fill="white")
            draw.text((20, self.height - 12), f"{hum:.1f} %", font=self.font, fill="white")

            # Graficas del historico
            self._dibujar_historial(draw, temp_hist, TEMP_MAX, 24, 12)
            self._dibujar_historial(draw, hum_hist, HUM_MAX, 24, 35)

    def _dibujar_historial(self, draw, datos, valor_max, alto, offset_y):
        for i in range(1, len(datos)):
            x1, x2 = i - 1, i
            y1 = escalar(datos[i - 1], valor_max, alto) + offset_y
            y2 = escalar(datos[i], valor_max, alto) + offset_y
            draw.line((x1, y1, x2, y2), fill="white")
