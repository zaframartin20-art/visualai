class EnvironmentEngine:

    def generar(self, emocion):

        if emocion["emocion"] == "Épica":

            return {
                "lugar": "Montañas",
                "hora": "Atardecer",
                "clima": "Nublado"
            }

        elif emocion["emocion"] == "Inspiradora":

            return {
                "lugar": "Bosque",
                "hora": "Golden Hour",
                "clima": "Despejado"
            }

        return {
            "lugar": "Ciudad",
            "hora": "Noche",
            "clima": "Lluvia"
        }


environment_engine = EnvironmentEngine()