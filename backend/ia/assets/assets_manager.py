from pathlib import Path


class AssetsManager:

    def carpeta(self):

        ruta = Path("assets/generated")

        ruta.mkdir(
            parents=True,
            exist_ok=True
        )

    def escena(self, numero):

        ruta = self.carpeta() / f"scene_{numero}"

        ruta.mkdir(
        exist_ok=True
    )

    

        return ruta


assets_manager = AssetsManager()