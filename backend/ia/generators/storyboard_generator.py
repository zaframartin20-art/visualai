class StoryboardGenerator:

    def generar(self, timeline, historia):

        storyboard = []

        for escena in timeline:

            storyboard.append({

                "escena": escena["escena"],

                "inicio": escena["inicio"],

                "fin": escena["fin"],

                "descripcion": historia

            })

        return storyboard


storyboard_generator = StoryboardGenerator()