from backend.ia.creative_ai import generar_conceptos


class AIManager:

    def generar_visuales(self, data):

        conceptos = generar_conceptos(data)

        return {
            "estado": "ok",
            "resultado": conceptos
        }


ai_manager = AIManager()