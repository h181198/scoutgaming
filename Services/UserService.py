from Models.UserModel import User as Model
from app import hashing


class UserService:
    @staticmethod
    def validate_user(session, username, password):
        user = UserService.get_user_by_name(session, username)
        hash_password = hashing.hash_value(password, "lameSalt")
        return user.password == hash_password

    @staticmethod
    def get_user_unicode_id(session, unicode_id):
        return session.query(Model).filter_by(id=int(unicode_id)).first()

    @staticmethod
    def get_user_by_name(session, username):
        return session.query(Model).filter_by(username=username).first()

