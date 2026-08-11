from dataclasses import dataclass


@dataclass
class RenderJob:

    escena: int

    asset: object

    prioridad: int

    estado: str = "pendiente"