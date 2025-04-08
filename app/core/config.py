from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    CLOUDINARY_CLOUD_NAME: str
    CLOUDINARY_API_KEY: str
    CLOUDINARY_API_SECRET: str
    DATABASE_URL: str
    FIREBASE_CREDENTIALS_FILE: str
    FIREBASE_DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
