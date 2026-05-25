import time
from lcd_display import LCD

def main():
    lcd = LCD()
    try:

        lcd.write("Te amo tanto", "Besos Fresita <3")
        while True:
            time.sleep(1)  
    except KeyboardInterrupt:
        print("\nPrueba terminada.")
    finally:
        lcd.close()

if __name__ == "__main__":
    main()
