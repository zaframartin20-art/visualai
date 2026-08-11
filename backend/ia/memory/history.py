from datetime import datetime


def guardar_historial(audio, analisis):

    return {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "bpm": audio["bpm"],
        "duracion": audio["duracion"],
        "emocion": analisis["emocion"]
    }