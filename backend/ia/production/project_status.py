class ProjectStatus:

    def resumen(self, escenas):

        return {

            "escenas": len(escenas),

            "prompts": len(escenas),

            "imagenes": len(escenas)

        }


project_status = ProjectStatus()