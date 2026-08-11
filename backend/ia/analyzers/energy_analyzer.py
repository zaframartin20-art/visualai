import librosa
import numpy as np


def analizar_energia(ruta_audio):

    # Cargar audio
    y, sr = librosa.load(ruta_audio, sr=None)

    # Calcular energía RMS
    rms = librosa.feature.rms(y=y)[0]

    energia_media = float(np.mean(rms))

    if energia_media < 0.05:
        nivel = "Baja"
    elif energia_media < 0.15:
        nivel = "Media"
    else:
        nivel = "Alta"

    return {
        "nivel": nivel,
        "valor": round(energia_media, 4)
    }