from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from Services.EquipmentService import EquipmentService
from Services.EmployeeService import EmployeeService
from Services.TransactionService import TransactionService
from Controllers import session

index_page = Blueprint('index', __name__)


@index_page.route('/')
def index():
    try:
        missing_equ = EquipmentService.find_missing(session)
        has_quit = EmployeeService.get_quit_employees(session)
        has_equipment = []
        for emp in has_quit:
            if len(TransactionService.find_current_equipment(session, emp.id)) > 0:
                has_equipment.append(emp)

        return render_template('Views/Home/index.html', missing_equipment=missing_equ, has_equipment=has_equipment,
                               old_equipment=[])
    except TemplateNotFound:
        abort(404)
