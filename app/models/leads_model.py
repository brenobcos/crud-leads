from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.configs.database import db


@dataclass
class Lead(db.Model):
    date_creation = datetime.now()
    visit_last = datetime.now()

    name: str
    email: str
    phone: str
    creation_date: str
    last_visit: str
    visits: int

    __tablename__ = "leads"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    creation_date = Column(DateTime, default=date_creation)
    last_visit = Column(DateTime, default=visit_last)
    visits = Column(Integer, default=1)
