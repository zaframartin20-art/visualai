from backend.ia.models.asset import Asset


class AssetsEngine:

    def crear(self, escena):

        return Asset(

            escena=escena.numero,

            tipo="imagen",

            ruta=f"assets/generated/scene_{escena.numero}.png",

            prompt=escena.prompt

        )


assets_engine = AssetsEngine()