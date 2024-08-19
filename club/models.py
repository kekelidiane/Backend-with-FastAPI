from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Club(Base):
    __tablename__ = "clubs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    domain = Column(String)
    responsible = Column(String)
    description = Column(String)

    # visuals = Column(String)  # Stocker comme str et gérer la conversion dans la sérialisation
