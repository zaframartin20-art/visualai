from backend.ia.models.scene import Scene


class SceneParser:

    def convertir(self, historia):

        escenas = []

        bloques = historia.split("###")

        numero = 1

        for bloque in bloques:

            if len(bloque.strip()) == 0:
                continue

            escena = Scene(

                numero=numero,

                inicio=0,

                fin=0,

                titulo=f"Escena {numero}",

                descripcion=bloque.strip(),

                emocion="Épica",

                camara="Drone",

                iluminacion="Láser",

                efectos=[],

                prompt=""

            )

            escenas.append(escena)

            numero += 1

        return escenas


scene_parser = SceneParser()