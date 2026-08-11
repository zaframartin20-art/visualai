from pydantic import BaseModel


class AnalysisResult(BaseModel):
    bpm: float
    energia: dict
    tonalidad: dict
    estructura: dict