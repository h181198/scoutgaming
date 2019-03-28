from flask import Blueprint, render_template, abort, redirect, url_for
from jinja2 import TemplateNotFound
from Services.DeleteService import DeleteService
from Services.EmployeeService import EmployeeService
from Services.DepartmentService import DepartmentService
from Views import session, database

employee_page = Blueprint('employee', __name__)


@employee_page.route('/employee')
def employee():
    try:
        data = EmployeeService.get_all_employees(session=session)
        department_data = DepartmentService.get_all_departments(session)
        department_list = DepartmentService.get_all_departments_json(database=database)
        return render_template('Views/Employee/index.html', data=data, department_data=department_data,
                               department_list=department_list)
    except TemplateNotFound:
        abort(404)


@employee_page.route('/employee/delete/<string:emp_id>', methods=['POST'])
def delete_employee(emp_id):
    try:
        DeleteService.delete_employee(session=session, emp_id=emp_id)
        return redirect(url_for('employee.employee'))
    except TemplateNotFound:
        abort(404)


@employee_page.route('/employee/update/<string:emp_id>/<string:emp_name>/<int:department_id>'
                     '/<string:emp_start_date>/<string:emp_end_date>')
def update_employee(emp_id, emp_name, department_id, emp_start_date, emp_end_date):
    try:
        EmployeeService.update_employee(session, emp_id, emp_name, department_id, emp_start_date, emp_end_date)
    except TemplateNotFound:
        abort(404)
