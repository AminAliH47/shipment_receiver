from pydantic_settings import BaseSettings


class EnvsConfig(BaseSettings):
    VERSION: str
    DEBUG: bool
    TZ: str

    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    REDIS_HOST: str
    REDIS_PORT: str

    WEATHER_API_URL: str
    WEATHER_APIKEY: str

    HTTP_PROXY: str

    class Config:
        case_sensitive = True
        env_file = '.env'
        extra = 'ignore'


envs = EnvsConfig()
