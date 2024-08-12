import pandas as pd
from src.db.database import database


async def read_db(file: str, values: dict[str:str]) -> pd.DataFrame:
    with open(file) as query:
        data = await database.fetch_all(query.read(), values)
    return pd.DataFrame([dict(i) for i in data])


async def update_db(file: str, values: list[dict[str:str]]) -> pd.DataFrame:
    with open(file) as query:
        await database.execute_many(query.read(), values)


async def setup_db():
    await update_db("src/db/sql/create_tables.sql", values=[{}])
    await update_db("src/db/sql/add_admin.sql", values=[{}])
    await update_db("src/db/sql/add_public_album.sql", values=[{}])
