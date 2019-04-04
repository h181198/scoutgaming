from sqlalchemy import Column, Integer, String, ForeignKey, DATE
from sqlalchemy.types import TIMESTAMP
from Models.BaseModel import Base
from sqlalchemy.sql import func


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    employee_id = Column(String, ForeignKey("employees.id"))
    equipment_id = Column(Integer, ForeignKey("equipments.id"))
    transfer_date = Column(DATE, default=func.now())

    def __repr__(self):
        return "<Transaction (id='%i', employee_id='%s', equipment_id='%i', transfer_date='%s') >" % \
               (self.id, self.employee_id, self.equipment_id, self.transfer_date)
