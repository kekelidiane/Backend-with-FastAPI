from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Innovation(Base):
    __tablename__ = "innovations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    innovation_type = Column(String)
    date = Column(DateTime, default=datetime.now(), onupdate=datetime.now)
    description = Column(String)

    # visuals = Column(String)  # Stocker comme str et gérer la conversion dans la sérialisation
