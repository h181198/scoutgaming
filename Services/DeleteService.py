from Services.TransactionService import TransactionService as TS
from Services.DepartmentService import DepartmentService as DS
from Services.EquipmentService import EquipmentService as EqS
from Services.EmployeeService import EmployeeService as EmS
from Services.ReceiptService import ReceiptService as RS


class DeleteService:
    # Delete a receipt return True if successful
    @staticmethod
    def delete_receipt(session, rec_id):
        receipt = RS.find_receipt(session, rec_id)
        if receipt is None:
            return False

        # Find all equipment with that receipt and replace with null
        equipment_list = EqS.get_all_equipments(session)
        for equ in equipment_list:
            if equ.receipt_id == rec_id:
                EqS.update_equipment(session, equ.id, equ.price, equ.currency, equ.model,
                                     equ.buy_date, None, equ.description, equ.note)

        session.delete(receipt)
        session.commit()
        return True

    # Remove department based on id return True if successful
    @staticmethod
    def delete_department(session, dep_id):
        department = DS.find_department(session, dep_id)

        if department is None:
            return False

        # Find employees with that department and update
        employee_list = EmS.get_all_employees(session)
        for emp in employee_list:
            if emp.department_id == dep_id:
                EmS.update_employee(session, emp.id,emp.employee_number, emp.name, None, emp.start_date, emp.end_date)

        session.delete(department)
        session.commit()
        return True

    # Delete equipment return True if successful
    @staticmethod
    def delete_equipment(session, equ_id):
        equipment = EqS.find_equipment(session, equ_id)
        if equipment is None:
            return False

        # Find all transactions for that equipment and delete them
        # No use in keeping transactions without equipment
        transaction_list = TS.get_all_transactions(session)
        for trans in transaction_list:
            if trans.equipment_id == equ_id:
                DeleteService.delete_transaction(session, trans.id)

        session.delete(equipment)
        session.commit()
        return True

    # Delete employee return true if successful
    @staticmethod
    def delete_employee(session, emp_id):
        employee = EmS.find_employee(session, emp_id)
        if employee is None:
            return False

        # Find all transactions with employee
        transaction_list = TS.get_all_transactions(session)
        for trans in transaction_list:
            if trans.employee_id == emp_id:
                # Change None to default value if wanted
                TS.update_transaction(session, trans.id, trans.equipment_id, None, None)

        session.delete(employee)
        session.commit()
        return True

    # Delete a Transaction return true if successful
    @staticmethod
    def delete_transaction(session, tra_id):
        transaction = TS.find_transaction(session, tra_id)

        if transaction is None:
            return False

        session.delete(transaction)
        session.commit()
        return True
