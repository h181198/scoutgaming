from sqlalchemy import Column, Integer, String, ForeignKey, DATE
from sqlalchemy.types import TIMESTAMP
from Models.BaseModel import Base
# This is only a test, not sure if it will be a part of the finished product like this


class Equipment(Base):
    __tablename__ = 'equipments'

    id = Column(Integer, primary_key=True)
    model = Column(String)
    buy_date = Column(DATE)
    receipt_id = Column(String, ForeignKey("receipts.id"))
    price = Column(Integer)
    description = Column(String)
    note = Column(String)

    def __repr__(self):
        return "<Equipment (id='%i', model='%s', buy_date='%s', receipt='%s', price='%i', description='%s', note='%s') >" % (self.id, self.model, self.buy_date, self.receipt, self.price, self.description, self.note)
