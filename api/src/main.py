from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.db import crud
from src.db.database import database
from src.images.v1 import router as images_router
from src.users.v1 import router as users_router

load_dotenv(override=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    await crud.setup_db()
    yield
    await database.disconnect()


app = FastAPI(
    title="Nimbus API",
    version="0.0.1",
    lifespan=lifespan,
)
app.include_router(images_router.router)
app.include_router(users_router.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/status")
async def get_status():
    return {"status": "ok"}


@app.get("/v1/auth/username/{username}/password/{password}")
async def authenticate_user(username: str, password: str) -> bool:
    user = await crud.read_db(
        "src/db/sql/get_user_auth.sql",
        values={"username": username, "password": password},
    )
    return not user.empty
