import board

I2C_ADDRESS = 0x3C

I2C_SCL = board.SCL
I2C_SDA = board.SDA
DHT_PIN = board.D23  # Tu pin de datos funcional

OLED_WIDTH = 128
OLED_HEIGHT = 64

TEMP_MAX = 50
HUM_MAX = 100
HIST_MAX_POINTS = 128
REFRESH_DELAY = 2  # segundos
ANIM_LIMIT = 2

ICON_TEMP_PATH = "icons/temp.bmp"
ICON_HUM_PATH = "icons/hum.bmp"
