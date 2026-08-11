def construir_story_prompt(data):

    return f"""
Crear un videoclip cinematográfico.

Género:
{data['genero']}

BPM:
{data['bpm']}

Emoción:
{data['emocion']}

Descripción:
{data['descripcion']}
"""