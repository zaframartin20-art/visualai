class AudioAgent:

    def evaluar(self, datos):

        bpm = datos["bpm"]

        energia = datos["energia"]["nivel"]

        if bpm >= 126 and energia == "Alta":

            return {

                "emocion":"Festival",

                "visual":"Epic",

                "camara":"Drone"

            }

        if energia == "Media":

            return {

                "emocion":"Inspiradora",

                "visual":"Cinemático",

                "camara":"Travelling"

            }

        return {

            "emocion":"Íntima",

            "visual":"Minimalista",

            "camara":"Close Up"

        }