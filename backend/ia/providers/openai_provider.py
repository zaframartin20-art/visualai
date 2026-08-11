from openai import OpenAI

from backend.core.config import settings


class OpenAIProvider:

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

        self.model = settings.OPENAI_MODEL

    def generar_conceptos(self, prompt):

        respuesta = self.client.responses.create(

            model=self.model,

            input=prompt

        )

        return respuesta.output_text