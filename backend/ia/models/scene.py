from dataclasses import dataclass


@dataclass
class Scene:

    numero: int

    inicio: float

    fin: float

    titulo: str

    descripcion: str

    emocion: str

    camara: str

    iluminacion: str

    efectos: list

    prompt: str

    movimiento: str = ""

    prioridad: int = 0