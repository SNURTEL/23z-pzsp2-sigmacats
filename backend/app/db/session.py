from sqlalchemy.orm import sessionmaker

from app.core.config import create_db_engine, create_db_engine_admin

engine = create_db_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

engine_admin = create_db_engine_admin()
SessionLocalAdmin = sessionmaker(autocommit=False, autoflush=False, bind=engine_admin)
