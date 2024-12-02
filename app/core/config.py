from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str
    SECRET_KEY: str
    base_url: str

    class Config:
        env_file = ".env"

settings = Settings()