from app import database
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Date

Base = declarative_base()

# This is only a test, not sure if it will be a part of the finished product like this


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)


    def __repr__(self):
        return "<Employee (id='%s', country='%s', unit='%s') >" % (self.id, self.country, self.unit)
