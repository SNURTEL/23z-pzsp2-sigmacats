import uuid

from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.tasks import basic_tasks
from app.models.user import User, UserRead, UserCreate
from app.core.authentication import auth_backend
from app.db.user_methods import get_user_manager

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

app = FastAPI()

# provides /login and /logout routers
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

# provides /register router
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@app.get("/celery")
async def celery_test() -> dict[str, str]:
    r = basic_tasks.test_celery.delay()
    return {"Queued task": f"{r}"}


@app.get("/db")
async def db_test(db: Session = Depends(get_db)) -> dict[str, str]:
    result = db.execute("SELECT table_name FROM all_tables").all()  # type: ignore
    return {"tables": str(result)}

