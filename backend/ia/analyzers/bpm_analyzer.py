import librosa


def analizar_bpm(ruta_audio):

    y, sr = librosa.load(ruta_audio, sr=None)

    tempo, _ = librosa.beat.beat_track(
        y=y,
        sr=sr
    )

    return round(float(tempo), 2)