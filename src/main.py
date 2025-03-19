from typing import Union

## FastAPI Imports ##
from fastapi import FastAPI
from pydantic import BaseModel

## Python Library Imports ##
from datetime import date

## Application Imports ##
from user.router import router as user_router
from pantry.router import router as pantry_router

app = FastAPI()

app.include_router(user_router)
app.include_router(pantry_router)

@app.get("/")
async def root():
    return {"message": "Hello, Flatbush!"}