from Services.ConnectionService import create_session
from Models.Receipt import Receipt as Model


# Add a receipt return True if successful
def add_receipt(supplement, year):
    if supplement is None or year is None:
        return False

    receipt = Model(supplement=supplement, year=year)
    session = create_session()
    session.add(receipt)
    session.commit()
    return True


# Delete a receipt return True if successful
def delete_receipt(rec_id):
    receipt = find_receipt(rec_id)

    if receipt is None:
        return False

    session = create_session()
    session.delete(receipt)
    session.commit()
    return True


# Get a list of all receipts
def get_all_receipts():
    return create_session().query(Model)


# Find receipt from id
def find_receipt(rec_id):
    return create_session().query().filter_by(id=rec_id).first()
