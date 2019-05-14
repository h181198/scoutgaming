from Services.EquipmentService import EquipmentService as EqS
from Services.EmployeeService import EmployeeService as EmS
from Services.TransactionService import TransactionService as TS
import datetime
import collections


class WarningService:
    # Method to get missing equipment
    @staticmethod
    def get_missing_equipment(session):
        return EqS.find_missing(session)

    # Method to find employees that has quit and still has equipment.
    # Return the last transaction of that equipment
    @staticmethod
    def get_quit_employee_with_equipment(session):
        has_quit = EmS.get_quit_employees(session)
        has_equipment = []
        quit_equipment = []
        for emp in has_quit:
            transactions = TS.find_current_equipment_transaction(session, emp.id)
            if len(transactions) > 0:
                has_equipment.append(emp)
                for tran in transactions:
                    quit_equipment.append(tran)

        return quit_equipment

    # Method to find employees with old equipment.
    # Return the last transaction of those equipments
    @staticmethod
    def get_old_equipment_employees(session):
        current_employees = EmS.get_current_employees(session)
        old_equipment = []
        current_date = datetime.datetime.now().date()
        interval = datetime.timedelta(days=-1461)

        for emp in current_employees:
            if emp.id != 1 and emp.id != 2 and emp.id != 3 and emp.id != 4:
                curr_eq_trans = TS.find_current_equipment_transaction(session, emp.id)

                for trans in curr_eq_trans:
                    eq = EqS.find_equipment(session, trans.equipment_id)
                    if (eq.buy_date - current_date) < interval:
                        old_equipment.append(trans)

        return old_equipment

    # Method to find employees without registered equipment
    # Return list of employees
    @staticmethod
    def get_employees_without_equipment(session):
        emp_list = []
        all_emp = EmS.get_current_employees(session)
        for emp in all_emp:
            if len(TS.find_current_equipment(session, emp.id)) == 0:
                emp_list.append(emp)

        return emp_list

    # Method to find equipment without employee
    # return list of equipment
    @staticmethod
    def get_equipment_without_employee(session):
        eq_list = []
        all_eq = EqS.get_all_equipments(session) 
        for eq in all_eq:
            if len(TS.find_equipment_transactions(session, eq.id)) == 0:
                eq_list.append(eq)

        return eq_list

    # Method that finds equipment older than 4 years
    # return list of equipment
    @staticmethod
    def get_old_equipment(session):
        current_date = datetime.datetime.now().date()
        interval = datetime.timedelta(days=-1461)
        result = []
        equipment_list = EqS.get_all_equipments(session)

        for eq in equipment_list:
            last_tran = TS.find_last_equipment_transaction(session, eq.id)
            is_gone = False
            if last_tran is not None:
                is_gone = last_tran.employee_id == 2 or last_tran.employee_id == 3 or last_tran.employee_id == 4
            if (eq.buy_date - current_date) < interval and not is_gone:
                result.append(eq)

        return result

    # Method that finds and return if any users have duplicate IDs
    # Return list of employees
    @staticmethod
    def get_duplicate_employeeids(session):
        employee_list = EmS.get_all_employees(session).all()[4:]
        result=[]
        for i in range(len(employee_list)):
            duplicate = WarningService.__find_duplicate(employee_list[i], employee_list[:i])
            if duplicate is not None:
                result.append(employee_list[i])
                result.append(duplicate)

        return result

    # Method to find if there is duplicate in rest of list
    # return the duplicates
    @staticmethod
    def __find_duplicate(item, emp_list):
        for equ in emp_list:
            if equ.employee_number == item.employee_number:
                return equ

        return None
