from fastapi import APIRouter

from user.schema import User, UserCreate

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

#TODO: Delete this once the router setup is confirmed to work.
fake_db = [
    {
        "id": 1,
        "first_name": "Q",
        "last_name": "Q",
        "email": "qthedude@gmail.com",
        "pronouns": "he/him",
        "pantry_id": 1,
        "password": "password",
    },
    {
        "id": 2,
        "first_name": "Khalid",
        "last_name": "Richards",
        "email": "kthedude@gmail.com",
        "pronouns": "they/them",
        "pantry_id": 2,
        "password": "password2",
    },
    {
        "id": 3,
        "first_name": "Mel",
        "last_name": "Bush",
        "email": "dokutaemh@gmail.com",
        "pronouns": "she/her",
        "pantry_id": 3,
        "password": "password3",
    }
]

# TODO: Definitely delete this; these should come back from an auto-incrementing field
# in the DB. Also, we don't want globals like this.
NEXT_USER_ID = 4
NEXT_PANTRY_ID = 4

@router.get("/")
async def get_users():
    return fake_db

@router.get("/{user_id}")
async def get_user_by_id(user_id: int):
    for user in fake_db:
        if user["id"] == user_id:
            return user
    return {"error": "User not found."}

# TODO: Currently, the password doesn't get stored. Need to figure that out.
@router.put("/")
async def create_user(user: UserCreate):
    global NEXT_USER_ID, NEXT_PANTRY_ID
    new_user = User(**user.model_dump(), id=NEXT_USER_ID, pantry_id=NEXT_PANTRY_ID)
    NEXT_USER_ID += 1
    NEXT_PANTRY_ID += 1
    fake_db.append(new_user.model_dump())
    return new_user.model_dump()