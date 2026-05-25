from lcd_utils import LCDController

def main():
    lcd = LCDController()
    try:
        print("Inicializando pantalla LCD...")
        lcd.clear()
        
        lcd.write("LCD Inicializado", line=0)
        
        print("Iniciando efecto de desplazamiento (scrolling)...")
        
        lcd.scroll_text("Este texto se desplaza hacia la izquierda!", line=1, delay=0.2, repeat=3)
        
    except Exception as e:
        print(f"Error detectado: {e}")
    finally:
        print("Limpiando y cerrando LCD de forma segura.")
        lcd.close()

if __name__ == "__main__":
    main()
