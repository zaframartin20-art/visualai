class VisualStyleEngine:

    def generar(self, emocion, analisis_musical):

        energia = analisis_musical["energia"]["nivel"]

        if emocion["emocion"] == "Épica":

            return {
                "paleta": "Azul y Naranja",
                "iluminacion": "Cinemática",
                "efectos": "Partículas, niebla, lens flare",
                "movimiento": "Rápido"
            }

        elif emocion["emocion"] == "Inspiradora":

            return {
                "paleta": "Dorado",
                "iluminacion": "Atardecer",
                "efectos": "Luz volumétrica",
                "movimiento": "Suave"
            }

        return {
            "paleta": "Fría",
            "iluminacion": "Oscura",
            "efectos": "Lluvia",
            "movimiento": "Lento"
        }


visual_style_engine = VisualStyleEngine()