from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    DATABASE: str 
    
    DEBUG: bool
    LOG_LEVEL: str
    LOG_FILE_NAME:str
    PORT: int
    HOST: str
    
    API_TITLE: str
    API_DESCRIPTION: str
    API_VERSION: str
    
    class Config:
        env_file = ".env"
        case_sensitive = True




settings = AppSettings()