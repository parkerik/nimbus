import os
import shutil
from uuid import uuid4

from fastapi import UploadFile
from src.db import crud

DIRECTORY = os.environ["BASE_DIRECTORY"]


async def get_albums() -> list[str]:
    data = await crud.read_db("src/db/sql/get_albums.sql", values={})
    if data.empty:
        return []
    return data["name"].tolist()


async def add_album(album: str) -> None:
    await crud.update_db("src/db/sql/add_album.sql", values=[{"album": album}])


async def delete_album(album: str) -> None:
    await crud.update_db("src/db/sql/delete_album.sql", values=[{"album": album}])
    shutil.rmtree(f"{DIRECTORY}/{album}")


async def get_images(album: str, sort_type: str, num_images: int, offset: int):
    if sort_type == "ASC":
        return await crud.read_db(
            "src/db/sql/get_images_asc.sql",
            values={
                "album": album,
                "num_images": num_images,
                "offset": offset,
            },
        )
    return await crud.read_db(
        "src/db/sql/get_images_desc.sql",
        values={
            "album": album,
            "num_images": num_images,
            "offset": offset,
        },
    )


async def add_image(album: str, user: str, upload_file: UploadFile) -> None:

    album_id = await crud.read_db(
        "src/db/sql/get_album_id.sql", values={"album": album}
    )
    user_id = await crud.read_db("src/db/sql/get_user_id.sql", values={"user": user})
    filepath = f"{DIRECTORY}/{album}/{str(uuid4())}.png"
    await crud.update_db(
        "src/db/sql/add_image.sql",
        values=[
            {
                "filepath": filepath,
                "user_id": user_id["id"].item(),
                "album_id": album_id["id"].item(),
            }
        ],
    )

    if not os.path.exists(f"{DIRECTORY}/{album}"):
        os.makedirs(f"{DIRECTORY}/{album}")

    with open(filepath, "wb+") as f:
        f.write(upload_file.file.read())
