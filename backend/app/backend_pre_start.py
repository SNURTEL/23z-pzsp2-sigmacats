import logging
import os

from sqlmodel import SQLModel
from sqlalchemy import String
from sqlalchemy.sql import text, bindparam
from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

from app.db.session import engine, engine_admin
from app.util.log import get_logger

# models HAVE to be imported beforehand for SQLModel.metadata.create_all to work
from app.models import dummy


logger = get_logger()

max_tries = int(os.environ.get("FASTAPI_DB_CONNECTION_TIMEOUT", default=120))
wait_seconds = int(os.environ.get("FASTAPI_DB_CONNECTION_RETRY_PERIOD", default=3))

oracle_user_username = os.environ.get("ORACLE_USER_USERNAME", default="user1")
oracle_user_password = os.environ.get("ORACLE_USER_USERNAME", default="user1")


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.ERROR),
)
def init() -> None:
    try:
        with engine_admin.connect() as connection:
            # ping the DB
            connection.execute("SELECT 1")
    except Exception as e:
        logger.warning(f"DB is offline: {e}")
        raise e


def create_users():
    with engine_admin.connect() as connection:
        with connection.begin():
            connection.execute(
                """
                alter session set \"_ORACLE_SCRIPT\"=true
                """
            )
            sql = text(
                f"CREATE USER IF NOT EXISTS {oracle_user_password} IDENTIFIED BY {oracle_user_password}"
            )
            connection.execute(sql)
            sql = text(
                f"GRANT CREATE SESSION TO {oracle_user_username}"
            )
            connection.execute(sql)
            sql = text(
                f"GRANT CREATE TABLE TO {oracle_user_username}"
            )
            connection.execute(sql)


def create_tables():
    # TODO this should be done with alembic
    SQLModel.metadata.create_all(engine)


def main() -> None:
    logger.info("Attempting connection to DB")
    init()
    logger.info("DB up & running! Creating user & tables if not present")
    create_users()
    create_tables()
    logger.info("Done setting up backend!")


if __name__ == "__main__":
    main()