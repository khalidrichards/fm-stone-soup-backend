import bcrypt
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database.base import engine, Base

class User(Base):
    """
    User
    ----
    This class defines the base user model for the Stone Soup Map. This should contain all of the
    information about a user in addition to any references to other tables that contain user
    data (e.g. pantry_id). This will also contain any other methods necessary to act on user
    objects.
    """
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String)
    last_name = Column(String)
    email: Mapped[str] = mapped_column(String, unique=True)
    pronouns: Mapped[str] = mapped_column(String)
    pantry_id: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)

    ## TODO: Revisit this logic and store the passwords a bit more securely.
    def verify_password(self, password: str) -> bool:
        """ Verifies that the password passed in is the correct password for a given user object."""
        pwhash = bcrypt.hashpw(password, self.password)
        return self.password == pwhash
    
class UserCreate():
    pass