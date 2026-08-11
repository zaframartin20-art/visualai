from backend.ia.scene.shot_generator import generar_plano
from backend.ia.scene.prompt_generator import generar_prompt
from backend.ia.scene.camera_director import camera_director
from backend.ia.prompts.prompt_composer import prompt_composer


class SceneEngine:

    def generar(self, 
                timeline, 
                historia, 
                estilo,
                ambiente,
                personaje):

        escenas = []

        for bloque in timeline:

            escena = {
                "inicio": bloque["inicio"],
                "fin": bloque["fin"],
                "tipo": bloque["tipo"],
                "descripcion": historia,
                "plano": generar_plano(bloque["tipo"])
            }

            escena["prompt"] = generar_prompt(escena)

            escena["prompt"] = prompt_composer.construir(
                escena
            )

            escenas.append(escena)

            camara = camera_director.decidir(
                bloque["tipo"]
            )

            escena["camara"] = camara
            escena["estilo"] = estilo
            escena["ambiente"] = ambiente
            escena["personaje"] = personaje

        return escenas


scene_engine = SceneEngine()