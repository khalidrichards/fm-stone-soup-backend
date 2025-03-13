from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field

## PantryItem Schema ##

class PantryItemBase(BaseModel):
    """
    PantryItemBase
    ----------
    This class defines the base pantry item model for the Stone Soup Map.
    Note that PantryItems, while created, are always associated with a pantry.
    """

    name: str = Field(min_length=1, max_length=50)
    quantity: Optional[int] = Field(ge=0)
    unit: Optional[str] = Field(min_length=1, max_length=16)
    other_measurement: Optional[str] = Field(min_length=1, max_length=16)
    notes: Optional[str] = Field(min_length=1, max_length=256)
    expiration_date: datetime.datetime = Field()
    pantry_id: int


class PantryItemCreate(PantryItemBase):
    """
    PantryItemCreate
    ----------
    This class defines the model for pantry item creation.
    """

    pass


class PantryItem(PantryItemBase):
    """
    PantryItemCreate
    ----------
    This class defines the model for a pantry item. Only after creation will pantry
    items have an id.
    """
    id: int

    class Config:
        orm_mode = True

## Pantry Schema ##
class PantryBase(BaseModel):
    """
    PantryBase
    ----------
    This class defines the base pantry model. The pantry model itself doesn't have
    a lot of fields since most of the heavy lifting is done in the PantryItem model.
    """
    last_updated: datetime.datetime = Field()
    user_id: int

class PantryCreate(PantryBase):
    """
    PantryCreate
    ----------
    This class defines the model for creating a new pantry. When a user is created,
    their associated pantry should also be created. When the pantry is created, the
    the user's current id should be passed into user_id, last_updated should be set
    to the time at creation, and pantry_items (see `Pantry` model) should be an empty
    list.
    """
    pass

class Pantry(PantryBase):
    """
    Pantry
    ------
    This class defines the pantry model.
    """
    id: int
    pantry_items: List[PantryItem] = []

    class Config:
        orm_mode = True