from flask import Flask
from Controllers.HomeController import index_page
from Controllers.ReceiptController import receipt_page
from Controllers.EmployeeController import employee_page
from Controllers.EquipmentController import equipment_page
from Controllers.DepartmentController import department_page
from Controllers.TransactionController import transaction_page

app = Flask(__name__)
app.register_blueprint(index_page)
app.register_blueprint(receipt_page)
app.register_blueprint(employee_page)
app.register_blueprint(equipment_page)
app.register_blueprint(department_page)
app.register_blueprint(transaction_page)

app.config['SECRET_KEY'] = 'lameKey'

if __name__ == '__main__':
    app.run(debug=True)
