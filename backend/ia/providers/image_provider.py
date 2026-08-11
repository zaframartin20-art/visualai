from abc import ABC, abstractmethod


class ImageProvider(ABC):

    @abstractmethod
    def generar(self, image_request):
        pass