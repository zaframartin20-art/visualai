from datetime import datetime

class VisualLogger:
   
    def registrar(evento):

      print(
        f"[{datetime.now()}] {evento}"
    )

    def info(self, mensaje):

        print(f"[VisualAI] {mensaje}")


        logger = VisualLogger()