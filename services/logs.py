from datetime import date
from sqlalchemy.orm import Session
from typing import List

from schemas.log_schema import LogCreate, Log
from models.logmodel import LogModel


def read_logs(db:Session, skip: int = 0, limit: int = 100) -> List[Log]:
    logs = db.query(LogModel).offset(skip).limit(limit).all()
    return logs


def create_log(db: Session, log: LogCreate) -> LogCreate:
    db_log = LogModel(calorie=log.calorie,
                      exercise_time=log.exercise_time, date=log.date)
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log
