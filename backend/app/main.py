from fastapi import FastAPI

from app.db.session import SessionLocal
from app.tasks import basic_tasks

app = FastAPI()


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@app.get("/celery")
async def celery_test() -> dict[str, str]:
    r = basic_tasks.test_celery.delay()
    return {"Queued task": f"{r}"}


@app.get("/db")
async def db_test() -> dict[str, str]:
    db = SessionLocal()
    result = db.execute("SELECT table_name FROM all_tables").all()  # type: ignore
    return {"tables": str(result)}
