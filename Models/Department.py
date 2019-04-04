from Models.BaseModel import Base
from sqlalchemy import Column, Integer, String


class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    country = Column(String)
    unit = Column(String)

    def __repr__(self):
        return "<Department (id='%s', country='%s', unit='%s') >" % (self.id, self.country, self.unit)
