from app.session import SessionLocal
from app.models.user import User, AccessToken
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyAccessTokenDatabase

from app.core.user_manager import UserManager


async def get_user_db():
    db = SessionLocal()
    yield SQLAlchemyUserDatabase(db, User)


async def get_access_token_db():
    db = SessionLocal()
    yield SQLAlchemyAccessTokenDatabase(db, AccessToken)


async def get_user_manager():
    db = get_user_db()
    yield UserManager(db)
