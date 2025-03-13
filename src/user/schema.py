from pydantic import BaseModel, Field


class UserBase(BaseModel):
    """
    UserBase
    ----
    This class defines the base user model for the Stone Soup Map. This should contain all of the
    information about a user in addition to any references to other tables that contain user
    data (e.g. pantry_id). This will also contain any other methods necessary to act on user
    objects.
    """
    first_name: str = Field(min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=50)
    email: str = Field(min_length=1, max_length=128)
    pronouns: str = Field(min_length=1, max_length=16)


class UserCreate(UserBase):
    """
    UserCreate
    ----
    This class defines the model for creating a new user. This is a subclass
    of UserBase (see above) and includes a password field. When users are created
    they should gain an id field and pantry_id field.
    """
    password: str = Field(min_length=8, max_length=128)


class User(UserBase):
    """
    User
    ----
    This class defines what a user is in the application context. Note that the
    password for a user is not included in this class. The user's id and pantry_id
    are included since it may be needed for operations.
    """
    id: int
    pantry_id: int

    class Config:
        orm_mode = True