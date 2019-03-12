from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Date

Base = declarative_base()

# This is only a test, not sure if it will be a part of the finished product like this


class Equipment(Base):
    __tablename__ = 'equipments'

    id = Column(Integer, primary_key=True)
    model = Column(String)
    buy_date = Column(Date)
    receipt = Column(String)
    price = Column(Integer)
    description = Column(String)
    note = Column(String)

    def __repr__(self):
        return "<Equipment (id='%s', model='%s', buy_date='%s', receipt='%s', price='%i', description='%s', note='%s') >" % (self.id, self.model, self.buy_date, self.receipt, self.price, self.description, self.note)
