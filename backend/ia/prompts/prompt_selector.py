from backend.ia.prompts.prompt_library import PROMPTS


class PromptSelector:

    def obtener(self, tema):

        return PROMPTS.get(
            tema.lower(),
            []
        )


prompt_selector = PromptSelector()