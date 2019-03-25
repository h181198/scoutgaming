from flask import Flask, render_template, redirect, url_for, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models.Employee import Employee
from Services import EquipmentService, EmployeeService, DepartmentService



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
    data = EmployeeService.get_all_employees(session)
    department_data = DepartmentService.get_all_departments(session)
    return render_template('Views/Employee/index.html', data=data, department_data=department_data)


@app.route('/employee/delete/<string:emp_id>', methods=['POST'])
def delete_employee(emp_id):
    EmployeeService.delete_employee(emp_id, session)
    return redirect(url_for('employee'))


@app.route('/employee/update/<string:emp_id>/<string:emp_name>/'
           '<string:emp_department>/<string:emp_start_date>/<string:emp_end_date>')
def update_employee(emp_id, emp_name, emp_department, emp_start_date, emp_end_date):
    EmployeeService.update_employee(emp_id, emp_name, emp_department, emp_start_date, emp_end_date, session)
    return redirect(url_for('employee'))


@app.route('/equipment')
def equipment():
    data = EquipmentService.get_all_equipment()
    return render_template('Views/Equipment/index.html', data=data)


@app.route('/receipt')
def receipt():
    return render_template('Views/Receipt/index.html')


@app.route('/transaction')
def transaction():
    return render_template('Views/Transaction/index.html')


@app.route('/department')
def department():
    return render_template('Views/Department/index.html')


if __name__ == '__main__':
    app.run(debug=True)
