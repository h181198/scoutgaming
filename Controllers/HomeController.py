from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from Services.WarningService import WarningService
from Controllers import session

warning_page = Blueprint('warning', __name__)


@warning_page.route('/')
def warning():
    try:
        missing_equ = WarningService.get_missing_equipment(session)
        quit_with_equipment = WarningService.get_quit_employee_with_equipment(session)
        old_employee_equipment = WarningService.get_old_equipment_employees(session)
        no_equipment = WarningService.get_employees_without_equipment(session)
        no_location = WarningService.get_equipment_without_employee(session)
        old_equipment = WarningService.get_old_equipment(session)

        has_warnings = len(missing_equ) > 0 or len(quit_with_equipment) > 0 or len(old_employee_equipment) > 0 or \
                       len(no_equipment) > 0 or len(no_location) > 0 or len(old_equipment) > 0

        return render_template('Views/Warning/index.html', missing_equipment=missing_equ,
                               quit_with_equipment=quit_with_equipment, old_equipment=old_equipment,
                               no_equipment=no_equipment, no_location=no_location,
                               old_employee_equipment=old_employee_equipment, has_warnings=has_warnings)
    except TemplateNotFound:
        abort(404)
