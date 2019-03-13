from Services.ConnectionService import create_session
from Models.Transaction import Transaction as Model
from Models.Employee import Employee
from Models.Equipment import Equipment


# Add a new Transaction return True if successful
def add_transaction(equipment_id, employee_id):
    session = create_session()

    if (session.query(Employee).filter_by(id=employee_id).first() is None
            or session.query(Equipment).filter_by(id=equipment_id).first() is None):
        return False

    transaction = Model(equipment_id=equipment_id, employee_id=employee_id)
    session.add(transaction)
    session.commit()
    return True


# Delete a Transaction return true if successful
def delete_transaction(tra_id):
    session = create_session()

    transaction = find_transaction(tra_id)

    if transaction is None:
        return False
    else:
        session.delete(transaction)
        session.commit()
        return True


# Get a list of all Transactions
def get_all_transactions():
    return create_session().query(Model)


# Find a Transaction from id
def find_transaction(tra_id):
    return create_session().query(Model).filter_by(id=tra_id).first()
