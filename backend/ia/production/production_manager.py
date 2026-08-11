class ProductionManager:

    def producir(self, proyecto):

        return {
            "estado": "producción iniciada",
            "escenas": proyecto["escenas"]
        }


production_manager = ProductionManager()