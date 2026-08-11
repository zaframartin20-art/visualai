from backend.ia.prompts.prompt_optimizer import prompt_optimizer
from backend.ia.prompts.prompt_selector import prompt_selector
from backend.ia.prompts.prompt_context import prompt_context


class PromptComposer:

    def construir(self, escena):

        contexto = prompt_context.construir(escena)

        prompt = escena["prompt"]

        prompt = prompt_optimizer.optimizar(prompt)

        extras = prompt_selector.obtener("festival")

        for extra in extras:
          prompt += f"\n{extra}"

        return prompt


prompt_composer = PromptComposer()