from backend.ia.render.priority_engine import priority_engine


class PriorityEngine:

    def calcular(self, escenas):

        for escena in escenas:

            if escena.numero in [3, 6]:

                escena.prioridad = 10

            else:

                escena.prioridad = 5

                escenas = priority_engine.calcular(escenas)


        return escenas


priority_engine = PriorityEngine()