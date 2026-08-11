from backend.ia.scene.scene_validator import scene_validator


class ProjectValidator:

    def validar(self, escenas):

        errores = {}

        for escena in escenas:

            resultado = scene_validator.validar(escena)

            if resultado:

                errores[escena.numero] = resultado

        return errores


project_validator = ProjectValidator()