class DirectorFeedback:

    def revisar(self, escenas):

        return {
            "aprobado": True,
            "escenas": len(escenas)
        }


director_feedback = DirectorFeedback()