class RenderManager:

    def ejecutar(self, trabajos):

        for trabajo in trabajos:

            trabajo.estado = "completado"

        return trabajos


render_manager = RenderManager()