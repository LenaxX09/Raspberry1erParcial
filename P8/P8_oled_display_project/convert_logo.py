import os
from PIL import Image

def preparar_logo():
    ruta_origen = "assets/logomoksoft.png"
    ruta_destino = "assets/logo.pbm"
    
    if not os.path.exists("assets"):
        os.makedirs("assets")
        print("Carpeta 'assets' creada. Coloca tu imagen 'logomoksoft.png' dentro.")
        return

    if not os.path.exists(ruta_origen):
        print(f"Error: No se encontró el archivo {ruta_origen}")
        return

    print(f"Procesando {ruta_origen}...")
    
    img = Image.open(ruta_origen).convert("1")
    
    img = img.resize((128, 64))
    
    img.save(ruta_destino)
    print(f"¡Éxito! Logo guardado en: {ruta_destino}")

if __name__ == "__main__":
    preparar_logo()
