from backend.ia.providers.image_provider import ImageProvider


class MockImageProvider(ImageProvider):

    def generar(self, image_request):

        return {
            "scene": image_request.escena,
            "image": f"scene_{image_request.escena}.png",
            "status": "generated"
        }


mock_image_provider = MockImageProvider()