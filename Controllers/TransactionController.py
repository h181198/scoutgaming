from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from Services.TransactionService import TransactionService
from Services.EquipmentService import EquipmentService
from Services.EmployeeService import EmployeeService
from Services.WarningService import WarningService

from Controllers import session

transaction_page = Blueprint('transaction', __name__)


@transaction_page.route('/transaction')
def transaction():
    try:
        data = TransactionService.get_all_transactions(session=session)
        equipment_data = EquipmentService.get_all_equipments(session=session)
        employee_data = EmployeeService.get_all_employees(session=session)
        return render_template('Views/Transaction/index.html', data=data, equipment_data=equipment_data,
                               employee_data=employee_data)
    except TemplateNotFound:
        abort(404)


@transaction_page.route('/transaction/missing')
def missing_transaction():
    try:
        data = WarningService.get_quit_employee_with_equipment(session)
        equipment_data = EquipmentService.get_all_equipments(session=session)
        employee_data = EmployeeService.get_all_employees(session=session)
        return render_template('Views/Transaction/index.html', data=data, equipment_data=equipment_data,
                               employee_data=employee_data)
    except TemplateNotFound:
        abort(404)


@transaction_page.route('/transaction/old')
def old_transaction():
    try:
        data = WarningService.get_old_equipment(session)
        equipment_data = EquipmentService.get_all_equipments(session=session)
        employee_data = EmployeeService.get_all_employees(session=session)
        return render_template('Views/Transaction/index.html', data=data, equipment_data=equipment_data,
                               employee_data=employee_data)
    except TemplateNotFound:
        abort(404)
