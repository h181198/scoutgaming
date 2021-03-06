from flask import Blueprint, render_template, abort, request, redirect, url_for
from flask_login import login_required
from jinja2 import TemplateNotFound
from Services.TransactionService import TransactionService
from Services.EquipmentService import EquipmentService
from Services.EmployeeService import EmployeeService
from Services.DeleteService import DeleteService
from Controllers import session
from Helpers.ControllerHelper import string_to_list, create_data, create_single_id

transaction_page = Blueprint('transaction', __name__)


@transaction_page.route('/transaction', methods=['POST', 'GET'])
@login_required
def transaction():
    try:
        data = request.form.get('data')

        if data is not None and len(data) > 0:
            data = string_to_list(session, data)
        else:
            data = TransactionService.get_all_transactions(session)

        equipment_data = EquipmentService.get_all_equipments(session)
        latest_transaction = TransactionService.create_current_owner_dict(session, equipment_data)
        equipment_dict = dict()

        for equ in equipment_data:
            description = "None"
            if equ.description is not None:
                description = equ.description
            equipment_dict[equ.id] = str(equ.id) + ", " + description + ", (" +\
                                     str(latest_transaction[equ.id]) + ")"
        employee_data = EmployeeService.get_all_employees(session)
        employee_dict = EmployeeService.create_employee_dropdown(session)

        employee_list = EmployeeService.get_all_employees_json(session)
        equipment_list = EquipmentService.get_all_equipments_json(session)
        return render_template('Views/Transaction/index.html', data=data, equipment_data=equipment_data,
                               employee_data=employee_data, equipment_list=equipment_list, employee_list=employee_list,
                               employee_dict=employee_dict, equipment_dict=equipment_dict)
    except TemplateNotFound:
        abort(404)


@transaction_page.route('/transaction/add', methods=['POST'])
@login_required
def add_transaction():
    try:
        TransactionService.add_transaction(session=session, equipment_id=int(request.form['equipment']),
                                           employee_id=int(request.form['employee']),
                                           transfer_date=request.form["transfer-date"])
        return redirect(url_for('transaction.transaction'))
    except TemplateNotFound:
        abort(404)
    return ""


@transaction_page.route('/transaction/update', methods=['POST'])
@login_required
def update_transaction():
    try:
        data = create_data(str(request.data.decode('utf8')))
        employee_id = data[2]
        if employee_id == '1':
            employee_id = None
        else:
            employee_id = int(employee_id)

        TransactionService.update_transaction(session, int(data[0]), int(data[1]), employee_id, data[3])
        return TransactionService.get_transaction_json(session, int(data[0]))
    except TemplateNotFound:
        abort(404)


@transaction_page.route('/transaction/delete', methods=['POST'])
@login_required
def delete_transaction():
    try:
        DeleteService.delete_transaction(session=session, tra_id=int(create_single_id(str(request.data))[0]))
    except TemplateNotFound:
        abort(404)
    return ""


@transaction_page.errorhandler(401)
def page_not_found(e):
    return redirect('login')
