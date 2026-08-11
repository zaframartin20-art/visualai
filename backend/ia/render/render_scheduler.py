from backend.ia.models.render_job import RenderJob


class RenderScheduler:

    def crear(self, escenas):

        trabajos = []

        for escena in escenas:

            trabajos.append(

                RenderJob(

                    escena=escena.numero,

                    asset=None,

                    prioridad=escena.prioridad

                )

            )

        return trabajos


render_scheduler = RenderScheduler()