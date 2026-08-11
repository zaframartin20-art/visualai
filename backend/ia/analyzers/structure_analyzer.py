def analizar_estructura(ruta_audio):

    return {
        "intro": [0, 32],
        "build": [32, 64],
        "drop": [64, 96],
        "break": [96, 128]
    }