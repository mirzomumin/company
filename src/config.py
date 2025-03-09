import os
from dotenv import load_dotenv


load_dotenv()


class Settings:
    DB_USER: str = os.environ["DB_USER"]
    DB_PASSWORD: str = os.environ["DB_PASSWORD"]
    DB_HOST: str = os.environ["DB_HOST"]
    DB_PORT: str = os.environ["DB_PORT"]
    DB_NAME: str = os.environ["DB_NAME"]
    DB_URL: str = (
        f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


settings = Settings()
