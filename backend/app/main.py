from fastapi import FastAPI

from app.db.session import SessionLocal
from app.tasks import basic_tasks

from app.util.log import get_logger

app = FastAPI()

logger = get_logger()


@app.get("/")
async def read_root() -> dict[str, str]:
    db = SessionLocal()
    result = db.execute("SELECT table_name FROM all_tables").all()  # type: ignore
    logger.info("ROOT")
    return {"tables": str(result)}


@app.get("/celery")
async def celery_test() -> dict[str, str]:
    r = basic_tasks.test_celery.delay()
    return {"Queued task": f"{r}"}
