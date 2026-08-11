import json


class JsonExporter:

    def exportar(self, escenas):

        datos = []

        for e in escenas:

            datos.append({

                "numero": e.numero,

                "inicio": e.inicio,

                "fin": e.fin,

                "titulo": e.titulo,

                "descripcion": e.descripcion,

                "prompt": e.prompt

            })

        return json.dumps(
            datos,
            indent=4,
            ensure_ascii=False
        )


json_exporter = JsonExporter()