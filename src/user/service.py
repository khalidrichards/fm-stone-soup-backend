from database.base import get_session
from .models import User

async def create_user(user: User):
    async with get_session() as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user