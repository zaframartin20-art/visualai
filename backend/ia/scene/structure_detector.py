def detectar_estructura(datos_audio):

    bpm = datos_audio["bpm"]

    if bpm < 100:
        estilo = "Lento"
    elif bpm < 125:
        estilo = "Medio"
    else:
        estilo = "Alta Energía"

    return {
        "estilo": estilo,
        "estructura": [
            "Intro",
            "Build Up",
            "Drop",
            "Break",
            "Drop Final",
            "Outro"
        ]
    }