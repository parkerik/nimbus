import os
from urllib.parse import quote_plus

import databases
from dotenv import load_dotenv

load_dotenv(override=True)

DATABASE_URL = (
    "postgresql+asyncpg://"
    f'{os.environ.get("DB_USERNAME", "postgres")}:'
    f'{quote_plus(str(os.environ.get("DB_PASSWORD", "postgres")))}@'
    f'{os.environ.get("DB_HOST", "0.0.0.0")}:{os.environ.get("DB_PORT", 5432)}/'
    f'{os.environ.get("DB_NAME", "postgres")}'
)

database = databases.Database(DATABASE_URL)
