from backend.ia.directors.camera_director import camera_director
from backend.ia.directors.lighting_director import lighting_director
from backend.ia.directors.effects_director import effects_director
from backend.ia.style.motion_director import motion_director


class VisualDirector:

    def dirigir(self, escenas):

        for escena in escenas:

            camera_director.asignar(escena)

            lighting_director.asignar(escena)

            effects_director.asignar(escena)

            motion_director.asignar(escena)

        return escenas


visual_director = VisualDirector()