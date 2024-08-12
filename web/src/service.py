import os

import requests
from dotenv import load_dotenv

load_dotenv(override=True)

BACKEND_PORT = 8000

DEV = os.environ.get("DEV", False).lower() == "true"
if DEV:
    BACKEND_ADDRESS = f"http://localhost:{BACKEND_PORT}"
else:
    BACKEND_ADDRESS = f"http://api:{BACKEND_PORT}"


def autheticate_user(username: str, password: str) -> bool:
    response = requests.get(
        f"{BACKEND_ADDRESS}/v1/auth/username/{username}/password/{password}"
    )
    if response.status_code == 200:
        return response.json()
    return False


def get_users():
    return requests.get(f"{BACKEND_ADDRESS}/v1/users").json()


def create_user(username: str, password: str):
    requests.post(f"{BACKEND_ADDRESS}/v1/users/{username}/password/{password}")


def delete_user(username: str):
    requests.delete(f"{BACKEND_ADDRESS}/v1/users/{username}")


def get_albums() -> list[str]:
    return requests.get(f"{BACKEND_ADDRESS}/v1/images/albums").json()


def create_album(album: str) -> list[str]:
    return requests.post(f"{BACKEND_ADDRESS}/v1/images/albums/{album}")


def delete_album(album: str):
    requests.delete(f"{BACKEND_ADDRESS}/v1/images/albums/{album}")


def get_images(album: str, sort_type: str, num_images: int, offset: int) -> list[str]:
    match sort_type:
        case "Oldest to Newest":
            sort_type = "ASC"
        case "Newest to Oldest":
            sort_type = "DESC"
        case _:
            sort_type = "ASC"

    return requests.get(
        f"{BACKEND_ADDRESS}/v1/images/albums/{album}/sort_type/{sort_type}/num_images/{num_images}/offset/{offset}"
    ).json()


def upload_image(album: int, user: int, image) -> None:
    requests.post(
        f"{BACKEND_ADDRESS}/v1/images/albums/{album}/users/{user}",
        files={"upload_file": image},
    )
