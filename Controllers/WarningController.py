from flask import Blueprint, render_template, abort, redirect
from flask_login import login_required
from jinja2 import TemplateNotFound
from Services.WarningService import WarningService
from Controllers import session
# Remove when testing is done
from collections import defaultdict
#import matplotlib.pyplot as plt
from Services.EquipmentService import EquipmentService

warning_page = Blueprint('warning', __name__)


@warning_page.route('/warning')
@login_required
def warning():
    try:
        missing_equ = WarningService.get_missing_equipment(session)
        quit_with_equipment = WarningService.get_quit_employee_with_equipment(session)
        old_employee_equipment = WarningService.get_old_equipment_employees(session)
        no_equipment = WarningService.get_employees_without_equipment(session)
        no_location = WarningService.get_equipment_without_employee(session)
        old_equipment = WarningService.get_old_equipment(session)

        create_economy_statistics()

        has_warnings = len(missing_equ) > 0 or len(quit_with_equipment) > 0 or len(old_employee_equipment) > 0 or \
                       len(no_equipment) > 0 or len(no_location) > 0 or len(old_equipment) > 0
        return render_template('Views/Warning/index.html', missing_equipment=missing_equ,
                               quit_with_equipment=quit_with_equipment, old_equipment=old_equipment,
                               no_equipment=no_equipment, no_location=no_location,
                               old_employee_equipment=old_employee_equipment, has_warnings=has_warnings)
    except TemplateNotFound:
        abort(404)


@warning_page.errorhandler(401)
def page_not_found(e):
    return redirect('login')


def create_economy_statistics():
    # Comment out after so that we don't have unnecessary API calls
    # Only have 1000 a month

    # result = EquipmentService.money_spent(session)
    return
    # Now we have setup the result we get from our function call on money_spent()
    # Move on to create a graph

    # plt.bar(*zip(*result.items()))
    # plt.savefig('./static/Pictures/Money_spent.png')
