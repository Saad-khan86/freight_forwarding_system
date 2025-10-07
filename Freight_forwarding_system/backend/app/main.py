from contextlib import asynccontextmanager
from fastapi import FastAPI
from .database import create_tables, engine
from .models import SQLModel
from .routers import users

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Creating Tables')
    create_tables()
    print("Tables Created")
    yield


app: FastAPI = FastAPI(
    lifespan=lifespan, title="dailyDo Todo App", version='1.0.0')

app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Freight Forwarding Backend is Live with SQLModel + UV!"}

@app.get("/all_user")
def get_user():
    return users.read_users()
    