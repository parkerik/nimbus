import os

from src.db import crud


async def get_users() -> list[str]:
    users = await crud.read_db("src/db/sql/get_users.sql", values={})
    return users["username"].tolist()


async def delete_user(username: str) -> None:
    images = await crud.read_db(
        "src/db/sql/get_user_images.sql", values={"username": username}
    )
    await crud.update_db("src/db/sql/delete_user.sql", values=[{"username": username}])
    if not images.empty:
        for image in images["filepath"].tolist():
            os.remove(image)


async def create_user(username: str, password: str) -> None:
    await crud.update_db(
        "src/db/sql/add_user.sql",
        values=[{"role": "user", "username": username, "password": password}],
    )
