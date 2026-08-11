from backend.ia.services.ai_manager import ai_manager
from backend.ia.story.template_loader import cargar_template
from backend.ia.story.creative_rules import CREATIVE_RULES
from backend.ia.scene.scene_parser import scene_parser
from backend.ia.scene.scene_enricher import scene_enricher
from backend.ia.visual.visual_director import visual_director
from backend.ia.visual.image_pipeline import image_pipeline


class StoryEngine:

    def generar(self, datos):

        # Cargar template
        template = cargar_template("story_prompt.txt")

        # Agregar reglas creativas
        prompt = CREATIVE_RULES + "\n\n" + template

        # Insertar datos de la canción
        prompt = prompt.format(
            genero=datos["musica"]["genero"],
            bpm=datos["musica"]["bpm"],
            emocion=datos["emocion"]["emocion"],
            duracion=datos["musica"]["duracion"]
        )

        # Generar historia con IA
        historia = ai_manager.generar(prompt)

        # Convertir historia en escenas
        escenas = scene_parser.convertir(historia)

        # Enriquecer escenas
        escenas = scene_enricher.enriquecer(escenas)
        
        escenas = visual_director.dirigir(escenas)

        imagenes = image_pipeline.ejecutar(
            escenas
        )

        return {
            "historia": historia,
            "escenas": escenas,
            "imagenes": imagenes
        }


story_engine = StoryEngine()