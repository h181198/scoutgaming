from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database = create_engine('postgres://postgres:admin@localhost:5432/mydatabase')
database.connect()

Base = declarative_base()


def create_session():
    Session = sessionmaker(database)
    session = Session()

    return session
