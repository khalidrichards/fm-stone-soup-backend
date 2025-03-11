from typing import Union

## FastAPi Imports ##
from fastapi import FastAPI
from pydantic import BaseModel

## Python Library Imports ##
from datetime import date

app = FastAPI()

class PantryItem(BaseModel):
    name: str
    quantity: int
    unit: str

@app.get("/")
def read_root():
    return {"Hello": "from Flatbush Mixtape's Tech Working Group!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/add/")
def add_item(item: PantryItem):
    return {
        "name": item.name,
        "quantity": item.quantity,
        "unit": item,
        "date_added": date.today()
    }