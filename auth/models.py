from gino import Gino
from sqlalchemy import Column, Integer, String, JSON

from database import db

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    full_name = Column(String)
    mail = Column(String(50), unique=True, nullable=False)
    phone = Column(String)
    address = Column(String)


class Participant(User):
    __tablename__ = 'participants'

    profession = Column(String)


class Admin(User):
    __tablename__ = 'admins'

    role = Column(JSON, default="des droits")
    

class SuperAdmin(User):
    __tablename__ = 'super_admins'

    role = Column(JSON, default="Il aura plus de role que l'admin")
