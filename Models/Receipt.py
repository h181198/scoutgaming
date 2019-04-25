from sqlalchemy import Column, Integer, String
from Models.BaseModel import Base


class Receipt(Base):
    __tablename__ = 'receipts'

    id = Column(Integer, primary_key=True)
    comb_id = Column(String)
    supplement = Column(String)
    year = Column(Integer)

    def __repr__(self):
        return "<Receipt (id='%r', comp_id='%s' supplement='%s', year='%r') >" % (self.id, self.comb_id,
                                                                                  self.supplement, self.year)
