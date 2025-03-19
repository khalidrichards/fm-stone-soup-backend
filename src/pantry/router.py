from fastapi import APIRouter, HTTPException
from typing import Dict, List
from .models import Pantry, PantryItem  # Assuming these are the correct imports
from .schema import PantryItemCreate  # Assuming this is the correct import

router = APIRouter()

# In-memory storage for pantries
pantries: Dict[int, Pantry] = {}

@router.post("/pantry/{pantry_id}/add")
async def add_pantry_item(pantry_id: str, pantry_item: PantryItemCreate):
    if pantry_id not in pantries:
        pantries[pantry_id] = []
    pantries[pantry_id].append(PantryItem(**pantry_item.dict()))
    return {"message": "Item added successfully"}

@router.get("/pantry/{pantry_id}")
async def get_pantry_contents(pantry_id: str):
    if pantry_id not in pantries:
        raise HTTPException(status_code=404, detail="Pantry not found")
    return {"pantry_id": pantry_id, "contents": pantries[pantry_id]}

@router.delete("/pantry/{pantry_id}/remove")
async def remove_pantry_item(pantry_id: str, pantry_item: PantryItemCreate):
    if pantry_id not in pantries:
        raise HTTPException(status_code=404, detail="Pantry not found")
    try:
        item_to_remove = PantryItem(**pantry_item.dict())
        pantries[pantry_id].remove(item_to_remove)
    except ValueError:
        raise HTTPException(status_code=404, detail="Item not found in pantry")
    return {"message": "Item removed successfully"}
