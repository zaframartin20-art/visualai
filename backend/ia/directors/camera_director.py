class CameraDirector:

    def asignar(self, escena):

        numero = escena.numero

        if numero == 1:
            escena.camara = "Drone FPV"

        elif numero == 2:
            escena.camara = "Travelling"

        elif numero == 3:
            escena.camara = "Orbit"

        elif numero == 4:
            escena.camara = "Handheld Cinematic"

        else:
            escena.camara = "Crane Shot"

        return escena


camera_director = CameraDirector()