from Models.Transaction import Transaction as Model
from Services.EquipmentService import EquipmentService as EqS
from Services.EmployeeService import EmployeeService as EmS


class TransactionService:
    # Add a new Transaction return True if successful, does not support adding already made transaction
    @staticmethod
    def add_transaction(session, equipment_id, employee_id):
        if (EmS.find_employee(session, employee_id) is None or
                EqS.find_equipment(session, equipment_id) is None):
            return False

        transaction = Model(equipment_id=equipment_id, employee_id=employee_id)
        session.add(transaction)
        session.commit()
        return True

    # Delete a Transaction return true if successful
    @staticmethod
    def delete_transaction(session, tra_id):
        transaction = TransactionService.find_transaction(session, tra_id)

        if transaction is None:
            return False
        else:
            session.delete(transaction)
            session.commit()
            return True

    # Get a list of all Transactions
    @staticmethod
    def get_all_transactions(session):
        return session.query(Model)

    # Find a Transaction from id
    @staticmethod
    def find_transaction(session, tra_id):
        return session.query(Model).filter_by(id=tra_id).first()
