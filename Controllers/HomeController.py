from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from Services.EquipmentService import EquipmentService
from Controllers import session

index_page = Blueprint('index', __name__)


@index_page.route('/')
def index():
    try:
        missing_equ = EquipmentService.find_missing(session)
        return render_template('Views/Home/index.html', missing_equipment=missing_equ)
    except TemplateNotFound:
        abort(404)
