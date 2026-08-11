class QualityEngine:

    def evaluar(self, escena):

        score = 100

        if len(escena["prompt"]) < 200:
            score -= 15

        if escena["tipo"] == "drop":
            score += 5

        return {
            "score": score
        }


quality_engine = QualityEngine()