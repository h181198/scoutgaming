from sqlalchemy import Column, Integer, String
from Models.BaseModel import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    is_active = True
    is_authenticated = True
    is_anonymous = False

    def __repr__(self):
        return "<User (id='%r', username='%s', password='%s')>" % (self.id, self.username, self.password)

    def get_id(self):
        return str(self.id).encode("utf-8").decode("utf-8")
