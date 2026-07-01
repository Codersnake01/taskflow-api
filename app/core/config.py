class Settings(BaseSettings):
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }

    DATABASE_URL: PostgresDsn
    SECRET_KEY: str