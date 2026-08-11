class EffectsDirector:

    def asignar(self, escena):

        escena.efectos = [

            "Volumetric Light",

            "Particles",

            "Smoke",

            "Lens Flare"

        ]

        return escena


effects_director = EffectsDirector()