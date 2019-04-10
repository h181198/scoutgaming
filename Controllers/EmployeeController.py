from flask import Blueprint, render_template, abort, redirect, url_for, request
from jinja2 import TemplateNotFound
from Services.DeleteService import DeleteService
from Services.EmployeeService import EmployeeService
from Services.DepartmentService import DepartmentService
from Helpers.HelpMethods import create_data, create_single_id
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


@employee_page.route('/employee/delete', methods=['POST'])
def delete_employee():
    try:
        DeleteService.delete_employee(session=session, emp_id=int(create_single_id(str(request.data))[0]))
    except TemplateNotFound:
        abort(404)
    return ""


@employee_page.route('/employee/update', methods=['POST'])
def update_employee():
    try:
        data = create_data(str(request.data))
        EmployeeService.update_employee(session, int(data[0]), data[1], data[2], int(data[3]), data[4], data[5])
        return EmployeeService.get_employee_json(session, data[0])
    except TemplateNotFound:
        abort(404)


@employee_page.route('/employee/quit')
def employee_equipment():
    try:
        data = EmployeeService.get_quit_employees(session,)
        department_data = DepartmentService.get_all_departments(session)
        department_list = DepartmentService.get_all_departments_json(database=database)
        return render_template('Views/Employee/index.html', data=data, department_data=department_data,
                               department_list=department_list)
    except TemplateNotFound:
        abort(404)

@employee_page.route('/employee/add', methods=['POST'])
def add_employee():
    try:
        data = create_data(str(request.data))
        employee = EmployeeService.add_employee(session, data[0], data[1], int(data[2]), data[3], data[4])
        return EmployeeService.get_employee_json(session=session, emp_id=employee.id)
    except TemplateNotFound:
        abort(404)
    return ""
