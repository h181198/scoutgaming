from flask import Blueprint, render_template, abort, redirect, url_for
from jinja2 import TemplateNotFound
from Services.EquipmentService import EquipmentService
from Services.DeleteService import DeleteService
from Controllers import session

equipment_page = Blueprint('equipment', __name__)


@equipment_page.route('/equipment')
def equipment():
    try:
        data = EquipmentService.get_all_equipments(session=session)
        return render_template('Views/Equipment/index.html', data=data)
    except TemplateNotFound:
        abort(404)


@equipment_page.route('/equipment/delete/<string:equ_id>', methods=['POST'])
def delete_equipment(equ_id):
    print(equ_id)
    try:
        DeleteService.delete_equipment(session=session, equ_id=int(equ_id))
        return redirect(url_for('equipment.equipment'))
    except TemplateNotFound:
        abort(404)

