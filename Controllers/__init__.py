from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Helpers.CurrencyConverter import CurrencyConverter

database = create_engine('postgres://stg_scout_inventory@stg_scout_inventory/stg_scout_inventory')
database.connect()

Session = sessionmaker(database)
session = Session()

converter = CurrencyConverter()
