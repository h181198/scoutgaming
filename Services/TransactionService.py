from Models.Transaction import Transaction as Model
from Services.EquipmentService import EquipmentService as EqS
from Services.EmployeeService import EmployeeService as EmS
import json


class TransactionService:
    # Add a new Transaction return transaction if successful
    @staticmethod
    def add_transaction(session, equipment_id=None, employee_id=None, transaction=None):
        if (EmS.find_employee(session, employee_id) is not None and
                EqS.find_equipment(session, equipment_id) is not None):
            transaction = Model(equipment_id=equipment_id, employee_id=employee_id)
            session.add(transaction)
            session.commit()
            return transaction

        if isinstance(transaction, Model):
            session.add(transaction)
            session.commit()
            return transaction

        return None

    # Update Transaction
    @staticmethod
    def update_transaction(session, tran_id, equ_id, emp_id):
        transaction = TransactionService.find_transaction(session, tran_id)

        if isinstance(emp_id, type(None)) or EmS.find_employee(session, emp_id) is not None:
            transaction.employee_id = emp_id
        if isinstance(equ_id, type(None)) or EqS.find_equipment(session, equ_id) is not None:
            transaction.equipment_id = equ_id

        session.commit()

    # Get a list of all Transactions
    @staticmethod
    def get_all_transactions(session):
        return session.query(Model)

    # Get a list of all transactions as json
    @staticmethod
    def get_all_transactions_json(database):
        data = database.execute("SELECT * FROM transactions")
        return json.dumps([dict(r) for r in data])

    # Get a list of all the transactions of one employee
    @staticmethod
    def find_employee_transactions(session, emp_id):
        return session.query(Model).filter_by(employee_id=emp_id).all()

    # Get a list of all transactions for an equipment
    @staticmethod
    def find_equipment_transactions(session, equ_id):
        return session.query(Model).filter_by(equipment_id=equ_id).all()

    # Get find all transactions for current equipment of an employee
    @staticmethod
    def find_current_equipment_transaction(session, emp_id):
        transactions = TransactionService.find_employee_transactions(session, emp_id)
        current_eq = []
        for trans in transactions:
            history = TransactionService.find_equipment_transactions(session, trans.equipment_id)
            if len(list(filter(lambda x: x.transfer_date > trans.transfer_date, history))) == 0:
                current_eq.append(trans)

        return current_eq

    # Find current equipment for an employee
    @staticmethod
    def find_current_equipment(session, emp_id):
        transactions = TransactionService.find_current_equipment_transaction(session, emp_id)
        current_equipment = []
        for tran in transactions:
            current_equipment.append(EqS.find_equipment(session, tran.equipment_id))

        return current_equipment

    # Find a Transaction from id
    @staticmethod
    def find_transaction(session, tra_id):
        return session.query(Model).filter_by(id=tra_id).first()
