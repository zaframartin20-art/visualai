import os
import shutil

UPLOAD_FOLDER = "backend/uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def guardar_audio(file):

    ruta = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(ruta, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "archivo": file.filename,
        "ruta": ruta
    }