import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time
from config import I2C_ADDRESS, WIDTH, HEIGHT, SCROLL_SPEED

class OLEDScroller:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.display = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, self.i2c, addr=I2C_ADDRESS)
        
        self.display.fill(0)
        self.display.show()
        
        self.image = Image.new("1", (WIDTH * 2, HEIGHT)) 
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.load_default()

    def scroll_text(self, text):
        self.draw.rectangle((0, 0, WIDTH * 2, HEIGHT), outline=0, fill=0)
        self.draw.text((0, 0), text, font=self.font, fill=255)
        
        bbox = self.draw.textbbox((0, 0), text, font=self.font)
        text_width = bbox[2] - bbox[0]
        
        for x in range(0, text_width + 1):
            cropped = self.image.crop((x, 0, x + WIDTH, HEIGHT))
            self.display.image(cropped)
            self.display.show()
            time.sleep(SCROLL_SPEED)

    def clear(self):
        self.display.fill(0)
        self.display.show()
