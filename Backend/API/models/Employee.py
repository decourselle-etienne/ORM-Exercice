from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Employee(Base):

    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(100))
    lastname = Column(String(100))
    salary = Column(Float)
    manager_id = Column(Integer)
