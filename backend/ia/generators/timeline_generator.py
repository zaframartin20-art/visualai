def generar_timeline(datos_audio):

    duracion = datos_audio["duracion"]

    escenas = []

    cantidad = 8

    tiempo = duracion / cantidad

    for i in range(cantidad):

        escenas.append({
            "escena": i + 1,
            "inicio": round(i * tiempo, 2),
            "fin": round((i + 1) * tiempo, 2)
        })

    return escenas