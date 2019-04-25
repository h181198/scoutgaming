from flask import Blueprint, render_template, abort, request, redirect, url_for
from jinja2 import TemplateNotFound
from Controllers import session
from Services.ReceiptService import ReceiptService
from Services.DeleteService import DeleteService
from Helpers.HelpMethods import create_data, create_single_id

receipt_page = Blueprint('receipt', __name__)


@receipt_page.route('/receipt')
def receipt():
    try:
        data = ReceiptService.get_all_receipts(session)
        return render_template('Views/Receipt/index.html', data=data)
    except TemplateNotFound:
        abort(404)


@receipt_page.route('/receipt/add', methods=['POST'])
def add_receipt():
    try:
        ReceiptService.add_receipt(session=session, supplement=request.form['supplement'],
                                   year=int(request.form['year']))
        return redirect(url_for('receipt.receipt'))
    except TemplateNotFound:
        abort(404)
    return ""


@receipt_page.route('/receipt/update', methods=['POST'])
def update_receipt():
    try:
        data = create_data(str(request.data.decode('utf8')))
        ReceiptService.update_receipt(session, int(data[0]), data[2], int(data[1]))
        return ReceiptService.get_receipt_json(session, int(data[0]))
    except TemplateNotFound:
        abort(404)


@receipt_page.route('/receipt/delete', methods=['POST'])
def delete_receipt():
    try:
        print(DeleteService.delete_receipt(session=session, rec_id=create_single_id(str(request.data))[0]))
    except TemplateNotFound:
        abort(404)
    return ""
