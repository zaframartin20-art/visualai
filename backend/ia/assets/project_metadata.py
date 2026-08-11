from datetime import datetime


def generar_metadata():

    return {

        "fecha": datetime.now().isoformat(),

        "version": "0.1",

        "motor": "VisualAI"

    }