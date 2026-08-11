from dataclasses import dataclass


@dataclass
class ImageRequest:

    escena: int

    prompt: str

    width: int = 1024

    height: int = 1024

    style: str = "cinematic"

    quality: str = "high"