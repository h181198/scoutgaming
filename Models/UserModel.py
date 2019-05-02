from sqlalchemy import Column, Integer, String, ForeignKey, DATE
from sqlalchemy.types import TIMESTAMP
from Models.BaseModel import Base
from sqlalchemy.sql import func


class User:
    id = 1
    unicode_id = ""
    username = "test"
    password = "test"
    is_active = True
    is_authenticated = True
    is_anonymous = False

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return "<User (username='%s', password='%s') >" % (self.username, self.password)

    def get_id(self):
        return str(self.id).encode("utf-8").decode("utf-8")
