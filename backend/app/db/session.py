from sqlalchemy.orm import sessionmaker

from app.core.config import create_db_engine

engine = create_db_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
