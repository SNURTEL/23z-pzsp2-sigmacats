import datetime
import uuid
from typing import Optional

from fastapi_users import schemas
from fastapi_users.db import SQLAlchemyBaseUserTableUUID

from app.base import Base
from sqlmodel import Field


class User(SQLAlchemyBaseUserTableUUID, Base):
    """
    This class needs to have the same fields
    as the one in the database
    """
    id: int = Field(primary_key=True)
    name: str = Field(max_length=50)
    surname: str = Field(max_length=50)
    email: str = Field(max_length=30)
    gender: Optional[bool] = None
    birth_date: Optional[datetime] = None


class UserRead(schemas.BaseUser[uuid.UUID]):
    name: str = Field(max_length=50)
    surname: str = Field(max_length=50)
    email: str = Field(max_length=30)
    gender: Optional[bool] = None
    birth_date: Optional[datetime] = None


class UserCreate(schemas.BaseUserCreate):
    name: str = Field(max_length=50)
    surname: str = Field(max_length=50)
    email: str = Field(max_length=30)
    gender: Optional[bool] = None
    birth_date: Optional[datetime] = None


class UserUpdate(schemas.BaseUserUpdate):
    name: str = Field(max_length=50)
    surname: str = Field(max_length=50)
    email: str = Field(max_length=30)
    gender: Optional[bool] = None
    birth_date: Optional[datetime] = None
