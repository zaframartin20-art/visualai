from backend.ia.providers.openai_provider import OpenAIProvider

provider = OpenAIProvider()

respuesta = provider.generar_conceptos("""

Quiero un videoclip de Big Room House.

128 BPM

Festival.

Emoción épica.

Duración 3 minutos.

""")

print(respuesta)