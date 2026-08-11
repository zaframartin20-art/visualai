from backend.ia.models.image_request import ImageRequest


class ImageBuilder:

    def construir(self, escena):

        return ImageRequest(

            escena=escena.numero,

            prompt=escena.prompt

        )


image_builder = ImageBuilder()