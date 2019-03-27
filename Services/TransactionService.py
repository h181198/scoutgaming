from Models.Transaction import Transaction as Model
from Services.EquipmentService import EquipmentService as EqS
from Services.EmployeeService import EmployeeService as EmS


class TransactionService:
    # Add a new Transaction return True if successful
    @staticmethod
    def add_transaction(session, equipment_id=None, employee_id=None, transaction=None):
        if (EmS.find_employee(session, employee_id) is not None and
                EqS.find_equipment(session, equipment_id) is not None):
            transaction = Model(equipment_id=equipment_id, employee_id=employee_id)
            session.add(transaction)
            session.commit()
            return True

        if isinstance(transaction, Model):
            session.add(transaction)
            session.commit()
            return True

        return False

    # Delete a Transaction return true if successful
    @staticmethod
    def delete_transaction(session, tra_id):
        transaction = TransactionService.find_transaction(session, tra_id)

        if transaction is None:
            return False

        session.delete(transaction)
        session.commit()
        return True

    # Update Transaction
    @staticmethod
    def update_transaction(session, tran_id, equ_id, emp_id):
        transaction = TransactionService.find_transaction(session, tran_id)

        if EmS.find_employee(session, emp_id) is not None:
            transaction.employee_id = emp_id
        if EqS.find_equipment(session, equ_id) is not None:
            transaction.equipment_id = equ_id

        session.commit()

    # Get a list of all Transactions
    @staticmethod
    def get_all_transactions(session):
        return session.query(Model)

    # Find a Transaction from id
    @staticmethod
    def find_transaction(session, tra_id):
        return session.query(Model).filter_by(id=tra_id).first()
