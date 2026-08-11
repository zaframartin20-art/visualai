from backend.ia.providers.openai_provider import OpenAIProvider

provider = OpenAIProvider()


class AIDirector:

    def generar_historia(self, prompt):

        return provider.generar_conceptos(prompt)


ai_director = AIDirector()