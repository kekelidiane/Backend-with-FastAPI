from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

from core.database import db

class Stage(db.Model):
    __tablename__ = "stages"

    id = Column(Integer, primary_key=True, index=True)
    post = Column(String)
    date_begin = Column(DateTime, default=datetime.now(), onupdate=datetime.now)
    date_end = Column(DateTime, default=datetime.now(), onupdate=datetime.now)
    duration = Column(Integer)
    domain = Column(String)
    entreprise = Column(String)
    remuneration_salary = Column(String)
    stage_type = Column(String)
    