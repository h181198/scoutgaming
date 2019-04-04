from sqlalchemy import Column, Integer, String, ForeignKey, DATE
from Models.BaseModel import Base
from sqlalchemy.sql import func


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    employee_number = Column(String)
    name = Column(String)
    department_id = Column(Integer, ForeignKey("departments.id"))
    start_date = Column(DATE, default=func.now())
    end_date = Column(DATE)

    def __repr__(self):
        return "<Employee (id='%i', employee_number='%s', name='%s', department_id='%i', " \
               "start_date='%s', end_date='%s') >" % \
               (self.id, self.employee_number, self.name, self.department_id, self.start_date, self.end_date)
