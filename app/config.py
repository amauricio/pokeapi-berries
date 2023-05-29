from pydantic import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    DEBUG: Optional[bool]
    PORT: Optional[int]
    
    CACHE_TYPE: Optional[str]
    CACHE_TIME: Optional[int]
    

    class Config:
        env_file = ".env"

settings = Settings()