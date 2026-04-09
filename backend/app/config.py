from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    anthropic_api_key: str
    app_env: str = "development"
    model: str = "claude-sonnet-4-6"

    class Config:
        env_file = ".env"


settings = Settings()
