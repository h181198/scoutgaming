from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database = create_engine('postgres://postgres:admin@localhost:5432/mydatabase')
database.connect()

Session = sessionmaker(database)
session = Session()
