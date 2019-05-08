from flask import Blueprint, render_template, abort, request, redirect, url_for
from flask_login import login_required
from jinja2 import TemplateNotFound
from Services.DepartmentService import DepartmentService
from Services.DeleteService import DeleteService
from Controllers import session
from Helpers.ControllerHelper import create_data, create_single_id

department_page = Blueprint('department', __name__)


@department_page.route('/department')
@login_required
def department():
    try:
        data = DepartmentService.get_all_departments(session=session)
        return render_template('Views/Department/index.html', data=data)
    except TemplateNotFound:
        abort(404)


@department_page.route('/department/add', methods=['POST'])
@login_required
def add_department():
    try:
        DepartmentService.add_department(session=session, unit=request.form['unit'], country=request.form['country'])
        return redirect(url_for('department.department'))
    except TemplateNotFound:
        abort(404)
    return ""


@department_page.route('/department/update', methods=['POST'])
@login_required
def update_department():
    try:
        data = create_data(str(request.data.decode('utf8')))
        DepartmentService.update_department(session, int(data[0]), data[1], data[2])
        return DepartmentService.get_department_json(session, int(data[0]))
    except TemplateNotFound:
        abort(404)


@department_page.route('/department/delete', methods=['POST'])
@login_required
def delete_department():
    try:
        DeleteService.delete_department(session=session, dep_id=int(create_single_id(str(request.data))[0]))
    except TemplateNotFound:
        abort(404)
    return ""


@department_page.errorhandler(401)
def page_not_found(e):
    return redirect('login')
