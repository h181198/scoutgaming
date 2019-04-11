from flask import Blueprint, render_template, abort, redirect, url_for, request
from jinja2 import TemplateNotFound
from Services.TransactionService import TransactionService
from Services.EmployeeService import EmployeeService
from Services.EquipmentService import EquipmentService
from Services.DeleteService import DeleteService
from Controllers import session
from Helpers.HelpMethods import string_to_list

equipment_page = Blueprint('equipment', __name__)


@equipment_page.route('/equipment', methods=['POST', 'GET'])
def equipment():
    try:
        data = request.form.get('data')

        if data is not None and len(data) > 0:
            data = string_to_list(session, data)
        else:
            data = EquipmentService.get_all_equipments(session=session)

        latest_transaction = dict()
        for equip in data:
            transaction = TransactionService.find_last_equipment_transaction(session, equip.id)
            if transaction is not None:
                latest_transaction[equip.id] = EmployeeService.find_employee(session, transaction.employee_id).name
            else:
                latest_transaction[equip.id] = "None"

        return render_template('Views/Equipment/index.html', data=data, latest_transaction=latest_transaction)
    except TemplateNotFound:
        abort(404)


@equipment_page.route('/equipment/delete/<string:equ_id>', methods=['POST'])
def delete_equipment(equ_id):
    try:
        DeleteService.delete_equipment(session=session, equ_id=int(equ_id))
        return redirect(url_for('equipment.equipment'))
    except TemplateNotFound:
        abort(404)
