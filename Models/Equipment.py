from sqlalchemy import Column, Integer, String, ForeignKey, DATE
from Models.BaseModel import Base


class Equipment(Base):
    __tablename__ = 'equipments'

    id = Column(Integer, primary_key=True)
    model = Column(String)
    buy_date = Column(DATE)
    receipt_id = Column(Integer, ForeignKey("receipts.id"))
    price = Column(Integer)
    currency = Column(String)
    description = Column(String)
    note = Column(String)

    def __repr__(self):
        return "<Equipment (id='%i', model='%s', buy_date='%s', receipt='%r', price='%r', currency='%s', " \
               "description='%s', note='%s') >" % \
               (self.id, self.model, self.buy_date, self.receipt_id, self.price,
                self.currency, self.description, self.note)
