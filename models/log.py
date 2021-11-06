class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, auto_increment=True)
    calorie = Column(Integer, nullable=False)
    exercise_time = Column(Integer, nullable=False)
    date = Column(Date, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

