from app.core.config.api import ApiConfig
from app.core.config.db import PostgresConfig
from app.core.config.redis import RedisConfig
from app.core.config.rabbitmq import RabbitMQConfig


class Settings:
    def __init__(self):
        self.api = ApiConfig()
        self.postgres = PostgresConfig()
        self.redis = RedisConfig()
        self.rabbitmq = RabbitMQConfig()

settings = Settings() 