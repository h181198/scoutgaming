from flask import Flask
from flask_admin import Admin, BaseView, expose
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_admin.contrib.sqla import ModelView
from Models.Department import Department
<<<<<<< HEAD
from Models.Equipment import Equipment
from Models.Employee import Employee
from Models.Receipt import Receipt
from Models.Transaction import Transaction
=======
from Models.Employee import Employee

>>>>>>> flaskAdminViews

app = Flask(__name__)
database = create_engine('postgres://postgres:admin@localhost:5432/mydatabase')
database.connect()

Session = sessionmaker(database)
session = Session()

<<<<<<< HEAD
# Comment in if you want it to create the database for you
# Base.metadata.create_all(database)

test_department = Department(country="Norway", unit="Oslo")
session.add(test_department)
session.commit()

test_employee = Employee(id="E23", name="Endre", department_id=test_department.id)
session.add(test_employee)
session.commit()

test_receipt = Receipt(id="newRec", supplement="UAB", year=2019)
session.add(test_receipt)
session.commit()

test_equipment = Equipment(model="Apple Pay", price=1992, description="make me", note="hehe")
session.add(test_equipment)
session.commit()

test_transaction = Transaction(equipment_id=test_equipment.id, employee_id=test_employee.id)
session.add(test_transaction)
session.commit()

myList = session.query(Department)

for a in myList:
    print(type(a))


@app.route('/')
def hello_world():
    return 'Hello World!'


=======
>>>>>>> flaskAdminViews
admin = Admin(app)
admin.add_view(ModelView(Department, session))
admin.add_view(ModelView())

if __name__ == '__main__':
    app.run(debug=True)
