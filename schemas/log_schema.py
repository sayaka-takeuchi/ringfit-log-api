from datetime import date
from pydantic import BaseModel


class LogBase(BaseModel):
    calorie: int
    exercise_time: int
    date: date


class LogCreate(LogBase):
    pass

    class Config:
        orm_mode = True


class Log(LogBase):
    pass

    class Config:
        orm_mode = True
