from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from Services.WarningService import WarningService
from Controllers import session

index_page = Blueprint('index', __name__)


@index_page.route('/')
def index():
    try:
        missing_equ = WarningService.get_missing_equipment(session)
        quit_with_equipment = WarningService.get_quit_employee_with_equipment(session)
        old_equipment = WarningService.get_old_equipment(session)

        return render_template('Views/Home/index.html', missing_equipment=missing_equ,
                               quit_with_equipment=quit_with_equipment, old_equipment=old_equipment)
    except TemplateNotFound:
        abort(404)
