from typing import Union

## FastAPI Imports ##
from fastapi import FastAPI
from pydantic import BaseModel

## Python Library Imports ##
from datetime import date

## Application Imports ##
from user.service import create_user

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "from Flatbush Mixtape's Tech Working Group!"}

@app.put("/users")
async def add_user():
    user = await create_user()
    return {"user": user}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}