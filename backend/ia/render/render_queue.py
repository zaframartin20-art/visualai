class RenderQueue:

    def crear(self, escenas):

        return sorted(

            escenas,

            key=lambda x: x.prioridad,

            reverse=True

        )


render_queue = RenderQueue()