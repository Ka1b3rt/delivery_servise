from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


class EnvBaseSettings(BaseSettings):
    class Config:
        env_file = BASE_DIR / ".env"


class ApiSettings(EnvBaseSettings):
    PROJECT_NAME: str
    API_PORT: int


class PostgreSettings(EnvBaseSettings):
    PG_HOST: str
    PG_PORT: int
    PG_USER: str
    PG_PASSWORD: str
    PG_DB: str
    PG_ECHO: bool
    PG_POOL_SIZE: int
    PG_MAX_OVERFLOW: int

    @property
    def DATABASE_ASYNC_URL(self):
        return f"postgresql+asyncpg://{self.PG_USER}:{self.PG_PASSWORD}@{self.PG_HOST}:{self.PG_PORT}/{self.PG_DB}"

    @property
    def DATABASE_SYNC_URL(self):
        return f"postgresql+psycopg2://{self.PG_USER}:{self.PG_PASSWORD}@{self.PG_HOST}:{self.PG_PORT}/{self.PG_DB}"


class RabbitMQSettings(EnvBaseSettings):
    RABBITMQ_HOST: str
    RABBITMQ_PORT: int
    RABBITMQ_MANAGEMENT_PORT: int
    RABBITMQ_USER: str
    RABBITMQ_PASSWORD: str
    RABBITMQ_VHOST: str


class RedisSettings(EnvBaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_USER: str
    REDIS_PASSWORD: str

    REDIS_QUEUE: int
    REDIS_RESULTS: int
    REDIS_CACHE: int

    def _get_redis_url(self, db: int):
        return f"redis://{self.REDIS_USER}:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}/{str(db)}"

    @property
    def REDIS_URL_QUEUE(self):
        return self._get_redis_url(self.REDIS_QUEUE)

    @property
    def REDIS_URL_RESULTS(self):
        return self._get_redis_url(self.REDIS_RESULTS)

    @property
    def REDIS_URL_CACHE(self):
        return self._get_redis_url(self.REDIS_CACHE)


class Settings(BaseSettings):
    api: ApiSettings = ApiSettings()
    postgres: PostgreSettings = PostgreSettings()
    redis: RedisSettings = RedisSettings()
    rabbitmq: RabbitMQSettings = RabbitMQSettings()


settings = Settings()

