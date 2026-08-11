from backend.ia.analyzers.audio_analyzer import analizar_audio
from backend.ia.generators.timeline_generator import generar_timeline
from backend.ia.generators.storyboard_generator import storyboard_generator
from backend.ia.director import director
from backend.ia.memory.history import guardar_historial
from backend.ia.music_engine import music_engine
from backend.ia.scene.scene_engine import scene_engine
from backend.ia.emotion.emotion_engine import emotion_engine
from backend.ia.style.visual_style_engine import visual_style_engine
from backend.ia.render.quality_engine import quality_engine
from backend.ia.visual.visual_planner import visual_planner
from backend.ia.assets.project_metadata import generar_metadata
from backend.ia.story.director_feedback import director_feedback
from backend.ia.style.environment_engine import environment_engine
from backend.ia.style.character_engine import character_engine



metadata = generar_metadata()


class VisualAIPipeline:

    def __init__(self):
        pass

    def ejecutar(self, ruta_audio):

        # 1. Analizar audio
        datos_audio = analizar_audio(ruta_audio)

        # 2. Analizar música
        analisis_musical = music_engine.analizar(ruta_audio)

        # 3. Director IA
        resultado = director.dirigir(
            datos_audio,
            analisis_musical,
            emocion
        )

        analisis = resultado["analisis"]
        historia = resultado["historia"]

        # 4. Timeline
        timeline = generar_timeline(datos_audio)

        # 5. Storyboard
        storyboard = storyboard_generator.generar(
            timeline,
            historia
        )

        escenas = scene_engine.generar(
            timeline,
            historia,
            estilo
        )

        # 6. Historial
        historial = guardar_historial(
            datos_audio,
            analisis
        )

        plan = visual_planner.planificar(
            historia
        )

        emocion = emotion_engine.analizar(
            analisis_musical
        )

        ambiente = environment_engine.generar(
            emocion
        )

        personaje = character_engine.generar(
           emocion
        )

        estilo = visual_style_engine.generar(
            emocion,
            analisis_musical
        )

        feedback = director_feedback.revisar(
            escenas
        )

        calidad = []

        for escena in escenas:
            calidad.append(
                quality_engine.evaluar(escena)
            )

        return {
            "audio": datos_audio,
            "musica": analisis_musical,
            "analisis": analisis,
            "historia": historia,
            "timeline": timeline,
            "escenas": escenas,
            "storyboard": storyboard,
            "historial": historial,
            "emocion": emocion,
            "estilo": estilo,
            "calidad": calidad,
            "plan_visual": plan,
            "feedback": feedback,
            "metadata": metadata,
            "ambiente": ambiente,
            "personaje": personaje,
        }


pipeline = VisualAIPipeline()