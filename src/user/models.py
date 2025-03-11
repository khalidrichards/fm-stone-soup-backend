import bcrypt
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    """
    User
    ----
    This class defines the user model for the Stone Soup Map. This should contain all of the
    information about a user in addition to any references to other tables that contain user
    data (e.g. pantry_id). This will also contain any other methods necessary to act on user
    objects.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    pronouns = Column(String)
    pantry_id = Column(Integer)
    password = Column(String)

    ## TODO: Revisit this logic and store the passwords a bit more securely.
    def verify_password(self, password: str) -> bool:
        """ Verifies that the password passed in is the correct password for a given user object."""
        pwhash = bcrypt.hashpw(password, self.password)
        return self.password == pwhash

