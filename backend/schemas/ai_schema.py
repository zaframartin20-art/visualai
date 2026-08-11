from pydantic import BaseModel


class AIRequest(BaseModel):
    nombre: str
    genero: str
    descripcion: str