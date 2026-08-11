from backend.ia.analyzers.audio_analyzer import analizar_audio
from backend.ia.analyzers.bpm_analyzer import analizar_bpm
from backend.ia.analyzers.energy_analyzer import analizar_energia
from backend.ia.analyzers.key_analyzer import analizar_tonalidad
from backend.ia.analyzers.structure_analyzer import analizar_estructura


class MusicEngine:

    def analizar(self, ruta_audio):

        audio = analizar_audio(ruta_audio)

        return {
            "audio": audio,
            "bpm": analizar_bpm(ruta_audio),
            "energia": analizar_energia(ruta_audio),
            "tonalidad": analizar_tonalidad(ruta_audio),
            "estructura": analizar_estructura(ruta_audio)
        }


music_engine = MusicEngine()