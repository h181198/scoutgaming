from flask import Blueprint, render_template, abort, request, redirect, url_for
from jinja2 import TemplateNotFound
from Services.TransactionService import TransactionService
from Services.EquipmentService import EquipmentService
from Services.EmployeeService import EmployeeService
from Services.DeleteService import DeleteService
from Controllers import session
from Helpers.HelpMethods import string_to_list, create_data, create_single_id

transaction_page = Blueprint('transaction', __name__)


@transaction_page.route('/transaction', methods=['POST', 'GET'])
def transaction():
    try:
        data = request.form.get('data')

        if data is not None and len(data) > 0:
            data = string_to_list(session, data)
        else:
            data = TransactionService.get_all_transactions(session)

        equipment_data = EquipmentService.get_all_equipments(session)
        employee_data = EmployeeService.get_all_employees(session)

        employee_list = EmployeeService.get_all_employees_json(session)
        equipment_list = EquipmentService.get_all_equipments_json(session)
        return render_template('Views/Transaction/index.html', data=data, equipment_data=equipment_data,
                               employee_data=employee_data, equipment_list=equipment_list, employee_list=employee_list)
    except TemplateNotFound:
        abort(404)


@transaction_page.route('/transaction/add', methods=['POST'])
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
def update_transaction():
    try:
        data = create_data(str(request.data.decode('utf8')))
        TransactionService.update_transaction(session, int(data[0]), int(data[1]), int(data[2]), data[3])
        return TransactionService.get_transaction_json(session, int(data[0]))
    except TemplateNotFound:
        abort(404)


@transaction_page.route('/transaction/delete', methods=['POST'])
def delete_transaction():
    try:
        DeleteService.delete_transaction(session=session, tra_id=int(create_single_id(str(request.data))[0]))
    except TemplateNotFound:
        abort(404)
    return ""
