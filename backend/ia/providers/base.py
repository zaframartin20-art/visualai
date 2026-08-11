from abc import ABC, abstractmethod


class AIProvider(ABC):

    @abstractmethod
    def generar_conceptos(self, prompt: str):
        pass