from backend.ia.prompts.prompt_optimizer import prompt_optimizer

class ScenePromptBuilder:

    def construir(self, escena):


      prompt = f"""
{escena.descripcion}

Camera:
{escena.camara}

Lighting:
{escena.iluminacion}

Effects:
{", ".join(escena.efectos)}
"""

      return prompt_optimizer.optimizar(prompt)