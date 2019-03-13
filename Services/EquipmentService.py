from Services.ConnectionService import create_session
from Models.Receipt import Receipt
from Models.Equipment import Equipment as Model


# Add new equipment, return True if successful
def add_equipment(price, model=None, buy_date=None, receipt_id=None, description=None, note=None):
    session = create_session()
    if not(receipt_id is None) and session.query(Receipt).filter_by(id=receipt_id).first() is None:
        return False

    equipment = Model(price, model, buy_date, receipt_id, description, note)
    session.add(equipment)
    session.commit()
    return True


# Delete equipment return True if successful
def delete_equipment(equ_id):
    equipment = find_equipment(equ_id)
    if equipment is None:
        return False

    session = create_session()
    session.delete(equipment)
    session.commit()
    return True


# Get a list of all equipment
def get_all_equipment():
    return create_session().query(Model)


# Find equipment from id
def find_equipment(equ_id):
    return create_session().query(Model).filter_by(id=equ_id).first()
