from datetime import datetime
from typing import List

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.base import engine, Base

class PantryItem(Base):
    """
    PantryItem
    ----------
    This class is used for items in a user's pantry. Rows in this table should represent
    an individual item within a pantry.
    """
    
    __tablename__ = "pantry_item"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    quantity: Mapped[int] = mapped_column(Integer)
    unit: Mapped[str] = mapped_column(String)
    other_measurement: Mapped[str] =  mapped_column(String)
    notes: Mapped[str] = mapped_column(String)
    pantry_id: Mapped[int] = mapped_column(ForeignKey("pantry.id"))

class Pantry(Base):
    """
    Pantry
    ------
    This class defines the pantry model for the Stone Soup Map app. This acts as a
    container for PantryItems (see above). Every time a new pantry item is added to
    a pantry, the last_updated field should be updated.
    """

    __tablename__ = "pantry"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    last_updated: Mapped[datetime] = mapped_column(DateTime)

    user_id = mapped_column(ForeignKey("user.id"))
    pantry_items: Mapped[List["PantryItem"]] = relationship(back_populates="pantry_item")

    def get_pantry_size(self):
        return self.pantry_items.count()