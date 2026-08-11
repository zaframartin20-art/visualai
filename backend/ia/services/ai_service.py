from backend.ia.providers.openai_provider import OpenAIProvider
from backend.ia.core.logger import registrar


class AIService:

    def __init__(self):

        registrar("Generando historia IA...")
        self.provider = OpenAIProvider()
        registrar("Historia generada.")

    def generar_texto(self, prompt):

        return self.provider.generar_conceptos(prompt)


ai_service = AIService()