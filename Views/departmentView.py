from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

department_page = Blueprint('department', __name__)


@department_page.route('/department')
def department():
    try:
        return render_template('Views/Department/index.html')
    except TemplateNotFound:
        abort(404)
