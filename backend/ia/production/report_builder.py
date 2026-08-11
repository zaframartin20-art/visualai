class ReportBuilder:

    def construir(self, proyecto):

        return {

            "estado": "OK",

            "escenas": proyecto["escenas"],

            "imagenes": proyecto["imagenes"]

        }


report_builder = ReportBuilder()