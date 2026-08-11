from backend.ia.story.story_engine import story_engine

datos = {
    "musica": {
        "genero": "Big Room House",
        "bpm": 128,
        "duracion": 210
    },
    "emocion": {
        "emocion": "Épica"
    }
}

historia = story_engine.generar(datos)

print("\n" + "=" * 60)
print("HISTORIA GENERADA POR VISUALAI")
print("=" * 60 + "\n")
print(historia)