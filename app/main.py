from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.database import db
from app.modules.accounts.presentation.login import router as login_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield db.create_db_and_tables()


app = FastAPI(lifespan=lifespan)

app.include_router(login_router)


@app.get('/')
async def heath_checker():
    return {'message': "I'm Alive."}
