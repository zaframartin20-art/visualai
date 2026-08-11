from backend.ia.pipeline import pipeline


def analizar_audio(ruta_audio):

    resultado = pipeline.ejecutar(ruta_audio)

    return resultado