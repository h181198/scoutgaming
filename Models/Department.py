from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

# This is only a test, not sure if it will be a part of the finished product like this


class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    country = Column(String)
    unit = Column(String)

    def __repr__(self):
        return "<Department (id='%s', country='%s', unit='%s') >" % (self.id, self.country, self.unit)
