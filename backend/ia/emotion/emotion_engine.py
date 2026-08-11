class EmotionEngine:

    def analizar(self, analisis_musical):

        energia = analisis_musical["energia"]["nivel"]

        if energia == "Alta":
            emocion = "Épica"

        elif energia == "Media":
            emocion = "Inspiradora"

        else:
            emocion = "Melancólica"

        return {
            "emocion": emocion
        }


emotion_engine = EmotionEngine()