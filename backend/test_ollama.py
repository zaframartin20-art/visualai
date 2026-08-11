from backend.ia.providers.ollama_provider import ollama_provider

respuesta = ollama_provider.generar_conceptos("""
Eres un director de videoclips.

Genera una historia cinematográfica para una canción:

Género: Big Room House
BPM: 128
Duración: 3 minutos
Emoción: Épica

Divide la historia en introducción, build-up, drop y cierre.
""")

print(respuesta)