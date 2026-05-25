from PIL import Image, ImageDraw, ImageFont
import board
import busio
import adafruit_ssd1306
import os

class OLEDDisplay:
    def __init__(self, width=128, height=64):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.disp = adafruit_ssd1306.SSD1306_I2C(width, height, i2c)
        self.width = width
        self.height = height
        
        self.disp.fill(0)
        self.disp.show()
        self.font = ImageFont.load_default()
        self.load_icons()

    def load_icons(self):
        base = os.path.dirname(__file__)
        self.temp_icon = Image.open(os.path.join(base, "icons", "temp.ico")).resize((16, 16)).convert("1")
        self.hum_icon = Image.open(os.path.join(base, "icons", "humidity.ico")).resize((16, 16)).convert("1")

    def update(self, temperature, humidity):
        image = Image.new("1", (self.width, self.height))
        draw = ImageDraw.Draw(image)
        image.paste(self.temp_icon, (0, 4))
        draw.text((24, 6), f"Temp: {temperature:.1f}C", font=self.font, fill=255)
        
        image.paste(self.hum_icon, (0, 32))
        draw.text((24, 34), f"Hum:  {humidity:.1f}%", font=self.font, fill=255)
        
        self.disp.image(image)
        self.disp.show()
