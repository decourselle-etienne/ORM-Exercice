from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Project(Base):

    __tablename__ = "project"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    project_reference = Column(String(100))
