from app.core.config.base import BaseConfig


class ApiConfig(BaseConfig):
    PROJECT_NAME: str
    API_PORT: int
    DEBUG: bool = False
    API_PREFIX: str = "/api"
    API_VERSION: str = "v1"
    
    @property
    def API_V1_STR(self) -> str:
        return f"{self.API_PREFIX}/{self.API_VERSION}" 