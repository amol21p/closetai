from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # App
    app_name: str = "ClosetAI API"
    debug: bool = False
    api_prefix: str = "/api"

    # Supabase
    supabase_url: str
    supabase_key: str
    supabase_service_key: str = ""

    # AI
    anthropic_api_key: str = ""
    openai_api_key: str = ""

    # Weather
    openweathermap_api_key: str = ""

    # Stripe
    stripe_secret_key: str = ""
    stripe_webhook_secret: str = ""

    # CORS
    cors_origins: list[str] = ["http://localhost:3000"]

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


@lru_cache()
def get_settings() -> Settings:
    return Settings()
