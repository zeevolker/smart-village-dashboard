from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    
    COOKIE_NAME: str = "svd_access_token"

    COOKIE_SECURE: bool = False

    COOKIE_SAMESITE: str = "lax"

    COOKIE_PATH: str = "/"

    COOKIE_MAX_AGE: int = 86400

    BACKEND_CORS_ORIGINS: str = "http://localhost:3000"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
