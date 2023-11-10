import os

from sqlalchemy import create_engine
from sqlalchemy.engine import URL, Engine
import sys
import oracledb

oracledb.version = "23.0.0.0"
sys.modules["cx_Oracle"] = oracledb


def create_db_engine() -> Engine:
    db_url = URL.create(
        drivername="oracle",
        username=os.environ.get("ORACLE_ADMIN_USERNAME"),
        password=os.environ.get("ORACLE_ADMIN_PASSWORD"),
        host=os.environ.get("ORACLE_HOST"),
        database=os.environ.get("ORACLE_DATABASE"),
        port=int(os.environ.get("ORACLE_PORT", default="1521")),
    )
    return create_engine(db_url)
