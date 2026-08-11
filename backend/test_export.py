from backend.ia.story.story_engine import story_engine
from backend.ia.export.json_exporter import json_exporter

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

resultado = story_engine.generar(datos)

print(
    json_exporter.exportar(
        resultado["escenas"]
    )
)