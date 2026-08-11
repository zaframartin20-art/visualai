import os

def crear_estructura_proyecto(nombre):

    base = os.path.join("projects", nombre)

    carpetas = [
        "audio",
        "imagenes",
        "prompts",
        "storyboard",
        "renders",
        "exportaciones"
    ]

    for carpeta in carpetas:
        os.makedirs(os.path.join(base, carpeta), exist_ok=True)

    return {
        "mensaje": "Proyecto preparado",
        "ruta": base
    }