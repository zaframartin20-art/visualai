import librosa

from backend.ia.analyzers.energy_analyzer import analizar_energia


def analizar_audio(ruta_audio):

    y, sr = librosa.load(ruta_audio)

    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

    duracion = librosa.get_duration(y=y, sr=sr)

    energia = analizar_energia(y)

    return {

        "bpm": round(float(tempo)),

        "duracion": round(float(duracion), 2),

        "energia": energia

    }