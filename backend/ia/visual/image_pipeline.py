from backend.ia.visual.image_builder import image_builder
from backend.ia.visual.image_manager import image_manager


class ImagePipeline:

    def ejecutar(self, escenas):

        imagenes = []

        for escena in escenas:

            request = image_builder.construir(
                escena
            )

            imagen = image_manager.generar(
                request
            )

            imagenes.append(imagen)

        return imagenes


image_pipeline = ImagePipeline()