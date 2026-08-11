class LightingDirector:

    def asignar(self, escena):

        numero = escena.numero

        if numero <= 2:
            escena.iluminacion = "Azul eléctrico"

        elif numero <= 4:
            escena.iluminacion = "Láser rojo"

        else:
            escena.iluminacion = "Fuegos artificiales"

        return escena


lighting_director = LightingDirector()