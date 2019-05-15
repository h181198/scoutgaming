from flask import Blueprint, render_template, abort, redirect, url_for, request
from jinja2 import TemplateNotFound
from Services.DeleteService import DeleteService
from Services.EmployeeService import EmployeeService
from Services.EquipmentService import EquipmentService
from Services.DepartmentService import DepartmentService
from Services.TransactionService import TransactionService
from flask_login import login_required
from Helpers.ControllerHelper import create_data, create_single_id, string_to_list
from Controllers import session, database

employee_page = Blueprint('employee', __name__)


@employee_page.route('/employee', methods=['POST', 'GET'])
@login_required
def employee():
    try:
        data = request.form.get('data')

        if data is not None and len(data) > 0:
            data = string_to_list(session, data)
        else:
            data = EmployeeService.get_all_employees(session=session)[4:]
        department_data = DepartmentService.get_all_departments(session)
        department_list = DepartmentService.get_all_departments_json(database=database)
        all_employee = EmployeeService.get_all_employees_json(session)
        return render_template('Views/Employee/index.html', data=data, department_data=department_data,
                               department_list=department_list, all_employee=all_employee)
    except TemplateNotFound:
        abort(404)


@employee_page.route('/employee/delete', methods=['POST'])
@login_required
def delete_employee():
    try:
        DeleteService.delete_employee(session=session, emp_id=int(create_single_id(str(request.data))[0]))
    except TemplateNotFound:
        abort(404)
    return ""


@employee_page.route('/employee/update', methods=['POST'])
@login_required
def update_employee():
    try:
        data = create_data(str(request.data.decode('utf8')))
        EmployeeService.update_employee(session, int(data[0]), data[1], data[2], int(data[3]), data[4], data[5])
        return EmployeeService.get_employee_json(session, data[0])
    except TemplateNotFound:
        abort(404)


@employee_page.route('/employee/add', methods=['POST'])
@login_required
def add_employee():
    try:
        EmployeeService.add_employee(session=session, employee_number=request.form['id'],
                                     name=request.form['name'], department_id=int(request.form['department']),
                                     start_date=request.form['start-date'], end_date=request.form['end-date'])
        return redirect(url_for('employee.employee'))
    except TemplateNotFound:
        abort(404)
    return ""


@employee_page.route('/employee/equipment/<int:emp_id>', methods=['GET'])
@login_required
def find_equipment_employee(emp_id):
    try:
        eq_list = TransactionService.find_current_equipment(session=session, emp_id=emp_id)
        equipment_json = "[\n"
        for eq in eq_list:
            equipment_json += EquipmentService.get_equipment_json(session, eq.id) + ",\n"

        equipment_json = equipment_json[:len(equipment_json)-2] + "]"
        return equipment_json
    except TemplateNotFound:
        abort(404)


@employee_page.errorhandler(401)
def page_not_found(e):
    return redirect('login')
