from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Helpers.CurrencyConverter import CurrencyConverter

database = create_engine('postgres://postgres:admin@localhost:5432/postgres')
database.connect()

Session = sessionmaker(database)
session = Session()

converter = CurrencyConverter()
