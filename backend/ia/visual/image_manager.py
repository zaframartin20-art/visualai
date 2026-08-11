from backend.ia.visual.image_provider_factory import image_provider_factory


class ImageManager:

    def generar(self, request):

        provider = image_provider_factory.obtener()

        return provider.generar(request)