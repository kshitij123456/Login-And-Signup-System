from sqlalchemy import Column, DATE, UniqueConstraint, INT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class silo_storage(Base):
    __tablename__ = "silo_storage"
    id = Column(INT, primary_key= True, autoincrement=True)
    silo_id = Column(VARCHAR(45), nullable= False)
    type_grain = Column(VARCHAR(45), nullable= False)
    capacity = Column(INT, nullable= False)
    silo_current_capacity = Column(INT, nullable= False)
