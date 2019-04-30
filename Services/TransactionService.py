from Models.Transaction import Transaction as Model
from Services.EquipmentService import EquipmentService as EqS
from Services.EmployeeService import EmployeeService as EmS
import json


class TransactionService:
    # Add a new Transaction return transaction if successful
    @staticmethod
    def add_transaction(session, equipment_id=None, employee_id=None, transfer_date=None, transaction=None):
        exists = (EmS.find_employee(session, employee_id) is not None and
                  EqS.find_equipment(session, equipment_id) is not None)

        if exists and transfer_date is not None and isinstance(transfer_date, str) and transfer_date != "":
            transaction = Model(equipment_id=equipment_id, employee_id=employee_id, transfer_date=transfer_date)
            session.add(transaction)
            session.commit()
            return transaction
        elif exists:
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
    def update_transaction(session, tran_id, equ_id, emp_id, transfer_date):
        transaction = TransactionService.find_transaction(session, tran_id)
        if isinstance(emp_id, type(None)) or EmS.find_employee(session, emp_id) is not None:
            transaction.employee_id = emp_id
        if isinstance(equ_id, type(None)) or EqS.find_equipment(session, equ_id) is not None:
            transaction.equipment_id = equ_id
        if isinstance(transfer_date, str) and transfer_date != "":
            transaction.transfer_date = transfer_date
        session.commit()

    # Get a list of all Transactions
    @staticmethod
    def get_all_transactions(session):
        return session.query(Model)

    # Get a list of all transactions as json
    @staticmethod
    def get_all_transactions_json(session):
        data = TransactionService.get_all_transactions(session)
        result_json = "["
        for tran in data:
            tran_json = TransactionService.get_transaction_json(session, tran.id)
            result_json += tran_json + ","

        return result_json[:len(result_json) - 1] + "]"

    @staticmethod
    def get_transaction_json(session, tran_id):
        tran = TransactionService.find_transaction(session, tran_id)
        eq = EqS.find_equipment(session, tran.equipment_id)
        emp = EmS.find_employee(session, tran.employee_id)
        eq_description, eq_buy, emp_name = ["None"] * 3

        if eq is not None:
            eq_description = eq.description
            eq_buy = eq.buy_date

        if emp is not None:
            emp_name = emp.name
        else:
            emp_name = ""

        my_json = {
            'id': tran.id,
            'equipment_id': "id" + str(eq.id),
            'equipment_description': eq_description,
            'buy_date': eq_buy,
            'employee_id': emp_name,
            'transfer_date': tran.transfer_date
        }
        return json.dumps(my_json, indent=4, sort_keys=False, default=str)

    # Get a list of all the transactions of one employee
    @staticmethod
    def find_employee_transactions(session, emp_id):
        return session.query(Model).filter_by(employee_id=emp_id).all()

    # Get a list of all transactions for an equipment
    @staticmethod
    def find_equipment_transactions(session, equ_id):
        return session.query(Model).filter_by(equipment_id=equ_id).all()

    # Get last transaction for an equipment
    @staticmethod
    def find_last_equipment_transaction(session, equ_id):
        transactions = TransactionService.find_equipment_transactions(session, equ_id)
        for trans in transactions:
            if len(list(filter(lambda x: x.transfer_date > trans.transfer_date, transactions))) == 0:
                return trans

        return None

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
