import json


class ProjectExporter:

    def exportar(self, proyecto):

        with open(
            "assets/project.json",
            "w",
            encoding="utf8"
        ) as f:

            json.dump(

                proyecto,

                f,

                indent=4,

                ensure_ascii=False

            )


project_exporter = ProjectExporter()