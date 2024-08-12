from fastapi import APIRouter, UploadFile
from fastapi.responses import ORJSONResponse
from src.images.v1 import service

router = APIRouter(
    prefix="/v1/images", tags=["images"], default_response_class=ORJSONResponse
)


@router.get("/albums")
async def get_albums() -> list[str]:
    return await service.get_albums()


@router.post("/albums/{album}")
async def add_albums(album: str):
    await service.add_album(album)


@router.delete("/albums/{album}")
async def delete_album(album) -> None:
    return await service.delete_album(album)


@router.get(
    "/albums/{album}/sort_type/{sort_type}/num_images/{num_images}/offset/{offset}"
)
async def get_images(
    album: str, sort_type: str, num_images: int, offset: int
) -> list[str]:
    images = await service.get_images(album, sort_type, num_images, offset)
    if images.empty:
        return []
    return images["filepath"].tolist()


@router.post("/albums/{album}/users/{user}")
async def add_image(album: str, user: str, upload_file: UploadFile):
    await service.add_image(album, user, upload_file)
