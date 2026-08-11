from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "VisualAI"

    VERSION: str = "0.1"

    DESCRIPTION: str = "AI Video Generator"

    OPENAI_API_KEY: str

    OPENAI_MODEL: str = "gpt-5.5"

    IMAGE_PROVIDER = "mock"

    IMAGE_WIDTH = 1024

    IMAGE_HEIGHT = 1024

    IMAGE_STYLE = "cinematic"

    IMAGE_QUALITY = "high"

    VIDEO_FPS = 30

    AI_PROVIDER = "ollama"

    MODEL = "qwen2.5:3b"

    class Config:
        env_file = ".env"


settings = Settings()