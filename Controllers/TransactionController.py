from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from Services.TransactionService import TransactionService
from Services.EquipmentService import EquipmentService
from Services.EmployeeService import EmployeeService

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
        has_quit = EmployeeService.get_quit_employees(session)
        data = []
        for emp in has_quit:
            transactions = TransactionService.find_current_equipment(session, emp.id)
            if len(transactions) > 0:
                for trans in transactions:
                    data.append(trans)

        equipment_data = EquipmentService.get_all_equipments(session=session)
        employee_data = EmployeeService.get_all_employees(session=session)
        return render_template('Views/Transaction/index.html', data=data, equipment_data=equipment_data,
                               employee_data=employee_data)
    except TemplateNotFound:
        abort(404)
