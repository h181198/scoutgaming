from app import database
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Date

Base = declarative_base()

# This is only a test, not sure if it will be a part of the finished product like this


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(String, ForeignKey("departments.id"))
    start_date = Column(Date)
    end_date = Column(Date)


    def __repr__(self):
        return "<Employee (id='%i', name='%s', department_id='%s', start_date='%s', end_date='%s') >" % (self.id, self.name, self.department_id, self.start_date, self.end_date)
