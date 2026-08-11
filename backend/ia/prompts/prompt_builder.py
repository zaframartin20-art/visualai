def construir_prompt(nombre, genero, descripcion, datos_audio):

    bpm = datos_audio.get("bpm", "Desconocido")
    duracion = datos_audio.get("duracion", "Desconocida")

    prompt = f"""
Eres un director creativo experto en videoclips musicales.

Información del proyecto:

Nombre: {nombre}
Género: {genero}
Descripción: {descripcion}

Datos de la canción:

- BPM: {bpm}
- Duración: {duracion} segundos

Genera:

1. Una historia cinematográfica.
2. Una dirección artística.
3. Una paleta de colores.
4. Ideas de movimientos de cámara.
5. Escenas para Intro, Build Up, Drop y Break.

La historia debe ser original y estar sincronizada con la música.
"""

    return prompt