from backend.ia.prompts.scene_prompt_builder import scene_prompt_builder


class SceneEnricher:

    def enriquecer(self, escenas):

        for escena in escenas:

            escena.prompt = scene_prompt_builder.construir(
                escena
            )

        return escenas


scene_enricher = SceneEnricher()