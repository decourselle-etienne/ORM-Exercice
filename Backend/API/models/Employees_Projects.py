from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Employees_Projects(Base):

    __tablename__ = "employees_projects"

    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer)
    project_id = Column(Integer)
    salary = Column(Float)
