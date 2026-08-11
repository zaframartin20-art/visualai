from pydantic import BaseModel


class ProjectCreate(BaseModel):
    nombre: str
    artista: str
    genero: str
    bpm: int


class ProjectResponse(ProjectCreate):
    id: int
    estado: str