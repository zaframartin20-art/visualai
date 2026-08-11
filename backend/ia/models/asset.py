from dataclasses import dataclass


@dataclass
class Asset:

    escena: int

    tipo: str

    ruta: str

    prompt: str

    estado: str = "pendiente"