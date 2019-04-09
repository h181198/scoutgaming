from sqlalchemy import Column, Integer, String
from Models.BaseModel import Base


class Receipt(Base):
    __tablename__ = 'receipts'

    id = Column(String, primary_key=True)
    supplement = Column(String)
    year = Column(Integer)

    def __repr__(self):
        return "<Receipt (id='%s', supplement='%s', year='%i') >" % (self.id, self.supplement, self.year)
