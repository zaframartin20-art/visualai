from backend.ia.agents.audio_agent import AudioAgent
from backend.ia.story.story_engine import story_engine


class DirectorAI:

    def __init__(self):
        self.audio_agent = AudioAgent()

    def dirigir(self, datos_audio, analisis_musical, emocion):

        analisis = self.audio_agent.evaluar(datos_audio)

        historia = story_engine.generar({
            "analisis": analisis,
            "musica": analisis_musical,
            "emocion": emocion
        })

        return {
            "analisis": analisis,
            "historia": historia
        }


director = DirectorAI()