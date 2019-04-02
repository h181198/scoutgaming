from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database = create_engine('postgres://localhost:5432/myDatabase')
database.connect()

Session = sessionmaker(database)
session = Session()
