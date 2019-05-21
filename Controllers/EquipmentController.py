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

        latest_transaction = TransactionService.create_current_owner_dict(session, data)

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
def add_equipment():
    try:
        receipt = request.form['receipt']
        supplement = request.form['supplement']
        year = request.form['year']
        link = request.form['link']

        if receipt == "1" and supplement != "" and year != "":
            new_receipt = ReceiptService.add_receipt(session=session, supplement=supplement, year=int(year), link=link)
            receipt = new_receipt.id
        else:
            receipt = int(receipt)

        employee = request.form['employee']
        if employee == '1':
            employee = None

        price = request.form['price']
        if price == "":
            price = "0"

        new_equipment = EquipmentService.add_equipment(session=session, price=int(price),
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


@equipment_page.errorhandler(401)
def page_not_found(e):
    return redirect('login')
