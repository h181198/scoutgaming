from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from Services.DepartmentService import DepartmentService
from Controllers import session

department_page = Blueprint('department', __name__)


@department_page.route('/department')
def department():
    try:
        data = DepartmentService.get_all_departments(session=session)
        return render_template('Views/department/index.html', data=data)
    except TemplateNotFound:
        abort(404)
