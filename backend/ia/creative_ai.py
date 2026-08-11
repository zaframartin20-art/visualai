from backend.ia.prompts.prompt_builder import construir_prompt
from backend.ia.providers.openai_provider import OpenAIProvider

provider = OpenAIProvider()


def generar_conceptos(data):

    datos_audio = {
        "bpm": 128,
        "duracion": 210
    }

    prompt = construir_prompt(
        data.nombre,
        data.genero,
        data.descripcion,
        datos_audio
    )

    return provider.generar_conceptos(prompt)