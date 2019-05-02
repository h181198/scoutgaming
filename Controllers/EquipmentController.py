from flask import Blueprint, render_template, abort, redirect, url_for, request
from flask_login import login_required
from jinja2 import TemplateNotFound
from Services.TransactionService import TransactionService
from Services.EmployeeService import EmployeeService
from Services.EquipmentService import EquipmentService
from Services.ReceiptService import ReceiptService
from Services.DeleteService import DeleteService
from Controllers import session
from Helpers.ControllerHelper import create_data, string_to_list

equipment_page = Blueprint('equipment', __name__)


@equipment_page.route('/equipment', methods=['POST', 'GET'])
@login_required
def equipment():
    try:
        data = request.form.get('data')
        employee_data = EmployeeService.get_all_employees(session=session)
        receipt_data = ReceiptService.get_all_receipts(session=session)
        receipt_list = ReceiptService.get_all_receipts_json(session)

        if data is not None and len(data) > 0:
            data = string_to_list(session, data)
        else:
            data = EquipmentService.get_all_equipments(session=session)

        latest_transaction = dict()
        for equip in data:
            transaction = TransactionService.find_last_equipment_transaction(session, equip.id)
            if transaction is not None:
                emp = EmployeeService.find_employee(session, transaction.employee_id)
                if emp is not None:
                    latest_transaction[equip.id] = emp.name
            else:
                latest_transaction[equip.id] = "None"

        return render_template('Views/Equipment/index.html', data=data, latest_transaction=latest_transaction,
                               employee_data=employee_data, receipt_data=receipt_data, receipt_list=receipt_list)
    except TemplateNotFound:
        abort(404)


@equipment_page.route('/equipment/delete', methods=['POST'])
@login_required
def delete_equipment():
    try:
        DeleteService.delete_equipment(session=session, equ_id=int(request.data))
        return redirect(url_for('equipment.equipment'))
    except TemplateNotFound:
        abort(404)


@equipment_page.route('/equipment/update', methods=['POST'])
@login_required
def update_equipment():
    try:
        data = create_data(str(request.data.decode('utf8')))
        EquipmentService.update_equipment(session, int(data[0]), int(data[1]), data[2], data[3], data[4], int(data[5]),
                                          data[6], data[7])
        return EquipmentService.get_equipment_json(session, data[0])
    except TemplateNotFound:
        abort(404)


@equipment_page.route('/equipment/add', methods=['POST'])
@login_required
def add_employee():
    try:
        receipt = request.form['receipt']
        if receipt == "None":
            receipt = None
        else:
            receipt = int(receipt)

        employee = request.form['employee']
        if employee == '1':
            employee = None

        new_equipment = EquipmentService.add_equipment(session=session, price=int(request.form['price']),
                                                       currency=request.form['currency'],
                                                       model=request.form['model'], buy_date=request.form['buy-date'],
                                                       receipt_id=receipt, description=request.form['description'],
                                                       note=request.form['note'])

        if employee is not None and request.form['transfer-date'] is not "":
            TransactionService.add_transaction(session=session, equipment_id=int(new_equipment.id),
                                               employee_id=int(employee),
                                               transaction=request.form['transfer-date'])
        return redirect(url_for('equipment.equipment'))
    except TemplateNotFound:
        abort(404)
    return ""
