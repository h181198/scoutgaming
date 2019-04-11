from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
from Services.TransactionService import TransactionService
from Services.EquipmentService import EquipmentService
from Services.EmployeeService import EmployeeService
from Controllers import session
from Helpers.HelpMethods import string_to_list

transaction_page = Blueprint('transaction', __name__)


@transaction_page.route('/transaction', methods=['POST', 'GET'])
def transaction():
    try:
        data = request.form.get('data')

        if data is not None and len(data) > 0:
            data = string_to_list(session, data)
        else:
            data = TransactionService.get_all_transactions(session=session)

        equipment_data = EquipmentService.get_all_equipments(session=session)
        employee_data = EmployeeService.get_all_employees(session=session)
        return render_template('Views/Transaction/index.html', data=data, equipment_data=equipment_data,
                               employee_data=employee_data)
    except TemplateNotFound:
        abort(404)


