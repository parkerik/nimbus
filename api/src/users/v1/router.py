from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from src.users.v1 import service

router = APIRouter(
    prefix="/v1/users", tags=["users"], default_response_class=ORJSONResponse
)


@router.get("")
async def get_users() -> list[str]:
    return await service.get_users()


@router.delete("/{username}")
async def get_users(username: str) -> None:
    await service.delete_user(username)


@router.post("/{username}/password/{password}")
async def get_users(username: str, password: str) -> list[str]:
    return await service.create_user(username, password)
