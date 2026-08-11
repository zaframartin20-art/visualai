from backend.core.config import IMAGE_PROVIDER
from backend.ia.providers.mock_image_provider import mock_image_provider


class ImageProviderFactory:

    def obtener(self):

        if IMAGE_PROVIDER == "mock":

            return mock_image_provider

        raise Exception("Proveedor no configurado")


image_provider_factory = ImageProviderFactory()