from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field

## PantryItem Schema ##

class PantryItemBase(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    quantity: Optional[int] = Field(ge=0)
    unit: Optional[str] = Field(min_length=1, max_length=16)
    other_measurement: Optional[str] = Field(min_length=1, max_length=16)
    notes: Optional[str] = Field(min_length=1, max_length=256)
    expiration_date: datetime.datetime = Field()

class PantryItemCreate(PantryItemBase):
    pantry_id: int

class PantryItem(PantryItemBase):
    id: int
    pantry_id: int

    class Config:
        orm_mode = True

## Pantry Schema ##
class PantryBase(BaseModel):
    last_updated: datetime.datetime = Field()
    user_id: int

class PantryCreate(PantryBase):
    pass

class Pantry(PantryBase):
    id: int
    pantry_items: List[PantryItem] = []

    class Config:
        orm_mode = True