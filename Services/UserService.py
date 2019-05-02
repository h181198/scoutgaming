from Models.User import User as Model
from flask_hashing import Hashing


class UserService:
    @staticmethod
    def validate_user(session, username, password):
        hashing = Hashing()
        user = UserService.get_user_by_name(session, username)
        if user is not None:
            return hashing.check_value(user.password, password, "lameSalt")

        return False

    @staticmethod
    def get_user_unicode_id(session, unicode_id):
        return session.query(Model).filter_by(id=int(unicode_id)).first()

    @staticmethod
    def get_user_by_name(session, username):
        return session.query(Model).filter_by(username=username).first()

