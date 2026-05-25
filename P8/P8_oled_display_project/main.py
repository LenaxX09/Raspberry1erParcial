import os
import time
from display_manager import OLEDDisplay
from utils import get_timestamp

def main():
    oled = OLEDDisplay()
    
    print("Inicializando OLED...")
    oled.show_text("Inicializando...", x=15, y=25)
    time.sleep(1.5)
    
    ruta_logo = "assets/logo.pbm"
    if os.path.exists(ruta_logo):
        print("Cargando logotipo en pantalla...")
        oled.show_logo(ruta_logo)
        time.sleep(3)
    else:
        print(f"Aviso: No se encontró '{ruta_logo}'. Saltando despliegue de logo.")
    
    print("Iniciando bucle de tiempo real. Presiona Ctrl+C para salir.")
    try:
        while True:
            now = get_timestamp()
            oled.show_text(f"SISTEMA OK\n{now}", x=10, y=10)
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nInterrupción detectada por el usuario.")
    finally:
        oled.power_off()
        print("Pantalla OLED limpia y apagada correctamente.")

if __name__ == "__main__":
    main()
