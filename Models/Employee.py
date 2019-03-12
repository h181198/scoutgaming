from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.types import TIMESTAMP
from Models.BaseModel import Base
from sqlalchemy.sql import func

# This is only a test, not sure if it will be a part of the finished product like this


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(String, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey("departments.id"))
    start_date = Column(TIMESTAMP, default=func.now())
    end_date = Column(TIMESTAMP)


    def __repr__(self):
        return "<Employee (id='%s', name='%s', department_id='%i', start_date='%s', end_date='%s') >" % (self.id, self.name, self.department_id, self.start_date, self.end_date)
