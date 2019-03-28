from flask import Flask
from Views.home import index_page
from Views.receiptView import receipt_page
from Views.employeeView import employee_page
from Views.equipmentView import equipment_page
from Views.departmentView import department_page
from Views.transactionView import transaction_page

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
