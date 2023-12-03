from app.models.base import Base
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyBaseAccessTokenTable


class AccessToken(SQLAlchemyBaseAccessTokenTable[int], Base):
    pass
