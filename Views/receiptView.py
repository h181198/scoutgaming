from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from Views import session

receipt_page = Blueprint('receipt', __name__)


@receipt_page.route('/receipt')
def receipt():
    try:
        return render_template('Views/Receipt/index.html')
    except TemplateNotFound:
        abort(404)
