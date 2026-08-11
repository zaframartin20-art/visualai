class ImageMetadata:

    def crear(self, escena):

        return {

            "scene": escena.numero,

            "camera": escena.camara,

            "lighting": escena.iluminacion,

            "effects": escena.efectos

        }


image_metadata = ImageMetadata()