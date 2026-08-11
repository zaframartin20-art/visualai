class PromptContext:

    def construir(self, escena):

        return {
            "emocion": escena.get("emocion"),
            "tipo": escena.get("tipo"),
            "plano": escena.get("plano"),
            "camara": escena.get("camara"),
            "estilo": escena.get("estilo")
        }


prompt_context = PromptContext()