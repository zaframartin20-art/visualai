class CameraDirector:

    def decidir(self, tipo):

        movimientos = {
            "intro": {
                "camara": "Drone",
                "movimiento": "Lento"
            },
            "build": {
                "camara": "Steadicam",
                "movimiento": "Forward"
            },
            "drop": {
                "camara": "FPV",
                "movimiento": "Rápido"
            },
            "break": {
                "camara": "Handheld",
                "movimiento": "Suave"
            }
        }

        return movimientos.get(
            tipo,
            {
                "camara": "Cinema",
                "movimiento": "Normal"
            }
        )


camera_director = CameraDirector()