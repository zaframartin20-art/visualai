import ollama


class OllamaProvider:

    def __init__(self):
        self.model = "qwen2.5:3b"

    def generar_conceptos(self, prompt):

        respuesta = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return respuesta["message"]["content"]


ollama_provider = OllamaProvider()