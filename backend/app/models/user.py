import uuid
from typing import Optional

from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTableUUID,
)
from fastapi_users import BaseUserManager, UUIDIDMixin
from fastapi import Request
from sqlalchemy.orm import DeclarativeBase
from app.db.session import SessionLocal
from fastapi_users.authentication import BearerTransport
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

SECRET = "SECRET"

class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass


class AccessToken(SQLAlchemyBaseAccessTokenTableUUID, Base):
    pass


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")

async def get_user_db():
    db = SessionLocal()
    yield SQLAlchemyUserDatabase(db, User)


async def get_access_token_db():
    db = SessionLocal()
    yield SQLAlchemyAccessTokenDatabase(db, AccessToken)
