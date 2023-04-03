
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASES_URL: str = 'mysql+pymysql://root:123456@localhost:3306/db_ORM_exercice'

engine = create_engine(SQLALCHEMY_DATABASES_URL, echo=True)

LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
