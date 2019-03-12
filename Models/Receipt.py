from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Date

Base = declarative_base()

# This is only a test, not sure if it will be a part of the finished product like this


class Receipt(Base):
    __tablename__ = 'receipts'

    id = Column(Integer, primary_key=True)
    supplement = Column(String)
    year = Column(Integer)

    def __repr__(self):
        return "<Receipt (id='%s', supplement='%s', year='%i') >" % (self.id, self.supplement, self.year)
