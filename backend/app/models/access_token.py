from app.base import Base
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyBaseAccessTokenTableUUID


class AccessToken(SQLAlchemyBaseAccessTokenTableUUID, Base):
    pass
