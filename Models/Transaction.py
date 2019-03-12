from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import DateTime

Base = declarative_base()

# This is only a test, not sure if it will be a part of the finished product like this


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    equipment_id = Column(Integer, ForeignKey("equipments.id"))
    transfer_date = Column(DateTime)

    def __repr__(self):
        return "<Department (id='%s', employee_id='%i', equipment_id='%i', transfer_date='%s') >" % (self.id, self.employee_id, self.equipment_id, self.transfer_date)
