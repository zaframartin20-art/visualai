from backend.ia.visual.visual_timeline import visual_timeline


class VisualTimeline:

    def generar(self, escenas):

        tiempo = 0

        escenas = visual_timeline.generar(
            escenas
        )

        for escena in escenas:

            escena.inicio = tiempo

            escena.fin = tiempo + 15

            tiempo += 15

        return escenas


visual_timeline = VisualTimeline()