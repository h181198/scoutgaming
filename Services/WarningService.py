from Services.EquipmentService import EquipmentService
from Services.EmployeeService import EmployeeService
from Services.TransactionService import TransactionService
import datetime


class WarningService:
    # Method to get missing equipment
    @staticmethod
    def get_missing_equipment(session):
        return EquipmentService.find_missing(session)

    # Method to find employees that has quit and still has equipment.
    # Return the last transaction of that equipment
    @staticmethod
    def get_quit_employee_with_equipment(session):
        has_quit = EmployeeService.get_quit_employees(session)
        has_equipment = []
        quit_equipment = []
        for emp in has_quit:
            transactions = TransactionService.find_current_equipment(session, emp.id)
            if len(transactions) > 0:
                has_equipment.append(emp)
                for tran in transactions:
                    quit_equipment.append(tran)

        return quit_equipment

    # Method to find employees with old equipment.
    # Return the last transaction of those equipments
    @staticmethod
    def get_old_equipment(session):
        current_employees = EmployeeService.get_current_employees(session)
        old_equipment = []
        current_date = datetime.datetime.now().date()
        interval = datetime.timedelta(days=-1461)

        for emp in current_employees:
            if emp.id != 1 and emp.id != 2 and emp.id != 3:
                curr_eq_trans = TransactionService.find_current_equipment(session, emp.id)

                for trans in curr_eq_trans:
                    eq = EquipmentService.find_equipment(session, trans.equipment_id)
                    if (eq.buy_date - current_date) < interval:
                        old_equipment.append(trans)

        return old_equipment
