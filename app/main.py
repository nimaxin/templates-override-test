import contextlib

from fastapi import FastAPI

from app.admin.services import register_admin
from app.db.services import engine
from app.product.models import Base


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def home():
    return {"admin": "127.0.0.1:8000/panel"}


register_admin(app)
