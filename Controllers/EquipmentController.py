from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from Services.EquipmentService import EquipmentService
from Controllers import session

equipment_page = Blueprint('equipment', __name__)


@equipment_page.route('/equipment')
def equipment():
    try:
        data = EquipmentService.get_all_equipments(session=session)
        return render_template('Views/Equipment/index.html', data=data)
    except TemplateNotFound:
        abort(404)
