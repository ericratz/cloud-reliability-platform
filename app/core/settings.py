from pydantic import BaseModel

class Settings(BaseModel):
    APP_NAME: str = "Cloud Reliability Platform"
    ENV: str = "local"
    METRICS_PREFIX: str = "crp"

settings = Settings()