from flask import Flask
from Controllers import session
from flask_hashing import Hashing
from flask_login import LoginManager
from Services.UserService import UserService
from Controllers.LoginController import login_page
from Controllers.ReceiptController import receipt_page
from Controllers.WarningController import warning_page
from Controllers.EmployeeController import employee_page
from Controllers.EquipmentController import equipment_page
from Controllers.DepartmentController import department_page
from Controllers.TransactionController import transaction_page

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

hashing = Hashing(app)


@login_manager.user_loader
def load_user(user_id):
    return UserService.get_user_unicode_id(session, user_id)


app.register_blueprint(login_page)
app.register_blueprint(warning_page)
app.register_blueprint(receipt_page)
app.register_blueprint(employee_page)
app.register_blueprint(equipment_page)
app.register_blueprint(department_page)
app.register_blueprint(transaction_page)

app.config['SECRET_KEY'] = 'lameKey'

if __name__ == '__main__':
    app.run(debug=True)
