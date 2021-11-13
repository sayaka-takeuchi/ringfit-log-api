from sqlalchemy import Column, Integer, DateTime, Date
from db import Base
from datetime import datetime


class LogModel(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    calorie = Column(Integer, nullable=False)
    exercise_time = Column(Integer, nullable=False)
    date = Column(Date, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
