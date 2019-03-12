from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

database = create_engine('postgres://localhost:5432/myDatabase')
database.connect()

Base = declarative_base()
