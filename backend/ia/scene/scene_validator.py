class SceneValidator:

    def validar(self, escena):

        errores = []

        if not escena.prompt:
            errores.append("Prompt vacío")

        if not escena.camara:
            errores.append("Sin cámara")

        if not escena.iluminacion:
            errores.append("Sin iluminación")

        return errores


scene_validator = SceneValidator()