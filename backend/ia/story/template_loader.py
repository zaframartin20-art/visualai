from pathlib import Path


def cargar_template(nombre):

    ruta = Path("backend/ia/prompts") / nombre

    with open(ruta, encoding="utf-8") as f:
        return f.read()