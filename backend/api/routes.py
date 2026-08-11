from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import UploadFile, File
from backend.ia.creative_ai import generar_conceptos
from backend.schemas.ai_schema import AIRequest
from backend.ia.services.manager import ai_manager
from backend.ia.pipeline import pipeline
from backend.services.analysis_service import analizar_audio


from backend.services.file_service import guardar_audio
from backend.schemas.project_schema import ProjectCreate
from backend.services.project_service import (
    crear_proyecto,
    obtener_proyectos,
    obtener_proyecto,
    eliminar_proyecto,
)

router = APIRouter()


@router.get("/")
async def inicio():
    return {"mensaje": "VisualAI funcionando"}


@router.get("/projects")
async def listar_proyectos():
    return obtener_proyectos()


@router.post("/projects")
async def nuevo_proyecto(project: ProjectCreate):
    return crear_proyecto(project)


@router.get("/projects/{id}")
async def buscar_proyecto(id: int):

    proyecto = obtener_proyecto(id)

    if proyecto is None:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    return proyecto


@router.delete("/projects/{id}")
async def borrar_proyecto(id: int):
    return eliminar_proyecto(id)

@router.post("/upload")
async def subir_audio(file: UploadFile = File(...)):
    return guardar_audio(file)

@router.get("/ia/demo")
async def demo_ia():

    return generar_conceptos(
        nombre="Feel the World",
        genero="Emotional Progressive House",
        descripcion="Canción sobre esperanza y superación"
    )

@router.post("/ia/generar")
async def generar_ideas(data: AIRequest):
    return generar_conceptos(data)

@router.post("/ia/generar")
async def generar_ideas(data: AIRequest):
    return ai_manager.generar_visuales(data)

@router.post("/analyze")
async def analizar(file: UploadFile = File(...)):

    resultado = pipeline.ejecutar(file.filename)

    return resultado

@router.post("/analyze")
async def analizar_audio_visual(file: UploadFile = File(...)):

    ruta = guardar_audio(file)

    resultado = pipeline.ejecutar(ruta["ruta"])

    return resultado

@router.post("/analysis")
async def analysis(file: UploadFile = File(...)):

    audio = guardar_audio(file)

    resultado = analizar_audio(audio["ruta"])

    return resultado