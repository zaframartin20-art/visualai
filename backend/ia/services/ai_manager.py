from backend.ia.services.provider_factory import obtener_provider


class AIManager:

    def __init__(self):
        self.provider = obtener_provider()

    def generar(self, prompt):
        return self.provider.generar_conceptos(prompt)


ai_manager = AIManager()