from sqlalchemy import Column, Integer, String
from Models.BaseModel import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<Users (id='%r', username='%s', password='%s')>" % (self.id, self.username, self.password)
