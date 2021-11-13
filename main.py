from typing import List

from fastapi import Depends, FastAPI, APIRouter
from sqlalchemy.orm import Session

from db import Base, SessionLocal, engine
from schemas.log_schema import LogCreate, Log
from services import logs


Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@app.get("/logs", operation_id="getLog", tags=["logs"], response_model=List[Log])
def read_logs(db: Session = Depends(get_db)):
    db_logs = logs.read_logs(db=db)
    return [Log.from_orm(log) for log in db_logs]


@app.post("/logs", operation_id="createLog", tags=["logs"], response_model=LogCreate)
def create_log(log: LogCreate, db: Session = Depends(get_db)):
    return LogCreate.from_orm(logs.create_log(db=db, log=log))
