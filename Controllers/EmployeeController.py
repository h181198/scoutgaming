from flask import Blueprint, render_template, abort, redirect, url_for, request
from jinja2 import TemplateNotFound
from Services.DeleteService import DeleteService
from Services.EmployeeService import EmployeeService
from Services.DepartmentService import DepartmentService
from Helpers.HelpMethods import create_data
from Controllers import session, database

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


@employee_page.route('/employee/update', methods=['POST'])
def update_employee():
    try:
        data = create_data(str(request.data))
        EmployeeService.update_employee(session, data[0], data[1], int(data[2]), data[3], data[4])
    except TemplateNotFound:
        abort(404)
    return ""
