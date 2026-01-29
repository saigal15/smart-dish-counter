from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Smart Dish Counter API"

settings = Settings()
