from pydantic import BaseSettings


class Settings(BaseSettings):
    airtable_api_key: str = ""
    airtable_base: str = ""
    database_url: str = ""

    class Config:
        env_file = ".env"