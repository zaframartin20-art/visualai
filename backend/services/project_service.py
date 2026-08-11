projects = []


def crear_proyecto(data):
    proyecto = {
        "id": len(projects) + 1,
        "nombre": data.nombre,
        "artista": data.artista,
        "genero": data.genero,
        "bpm": data.bpm,
        "estado": "Nuevo"
    }

    projects.append(proyecto)

    return proyecto


def obtener_proyectos():
    return projects


def obtener_proyecto(id: int):
    for proyecto in projects:
        if proyecto["id"] == id:
            return proyecto

    return None


def eliminar_proyecto(id: int):

    for proyecto in projects:

        if proyecto["id"] == id:
            projects.remove(proyecto)
            return {"mensaje": "Proyecto eliminado"}

    return {"error": "Proyecto no encontrado"}