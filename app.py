from flask import Flask, render_template, redirect, url_for, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Services.EquipmentService import EquipmentService
from Services.DepartmentService import DepartmentService
from Services.EmployeeService import EmployeeService
from Services.TransactionService import TransactionService
import json


app = Flask(__name__)

database = create_engine('postgres://postgres:admin@localhost:5432/postgres')
database.connect()

app.config['SECRET_KEY'] = 'lameKey'

Session = sessionmaker(database)
session = Session()


@app.route('/')
def index():
    return render_template('Views/index.html')


@app.route('/employee')
def employee():
    data = EmployeeService.get_all_employees(session=session)
    department_data = DepartmentService.get_all_departments(session)
    data2 = database.execute("SELECT * FROM departments")
    print(data2)
    return render_template('Views/Employee/index.html', data=data, department_data=department_data, data2=json.dumps([dict(r) for r in data2]))


@app.route('/employee/delete/<string:emp_id>', methods=['POST'])
def delete_employee(emp_id):
    EmployeeService.delete_employee(session=session, emp_id=emp_id)
    return redirect(url_for('employee'))


@app.route('/employee/update/<string:emp_id>/<string:emp_name>/<string:emp_department>/<string:emp_start_date>/<string:emp_end_date>')
def update_employee(emp_id, emp_name, emp_department, emp_start_date, emp_end_date):
    department_id = DepartmentService.find_department(session=session, unit=emp_department)
    EmployeeService.update_employee(session, emp_id, emp_name, department_id, emp_start_date, emp_end_date)
    return redirect(url_for('employee'))


@app.route('/equipment')
def equipment():
    data = EquipmentService.get_all_equipment(session=session)
    return render_template('Views/Equipment/index.html', data=data)


@app.route('/receipt')
def receipt():
    return render_template('Views/Receipt/index.html')


@app.route('/transaction')
def transaction():
    data = TransactionService.get_all_transactions(session=session)
    equipment_data = EquipmentService.get_all_equipment(session=session)
    employee_data = EmployeeService.get_all_employees(session=session)
    return render_template('Views/Transaction/index.html', data=data, equipment_data=equipment_data, employee_data=employee_data)


@app.route('/department')
def department():
    return render_template('Views/Department/index.html')


if __name__ == '__main__':
    app.run(debug=True)
