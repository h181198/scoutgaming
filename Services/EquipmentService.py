from Models.Equipment import Equipment as Model
from Services.ReceiptService import ReceiptService as RS
import datetime


class EquipmentService:
    # Add new equipment, return True if successful
    @staticmethod
    def add_equipment(session, price=None, model=None, buy_date=None, receipt_id=None,
                      description=None, note=None, equipment=None):
        is_correct_instance = (isinstance(price, int) and
                               isinstance(model, (str, type(None))) and
                               isinstance(receipt_id, (str, type(None))) and
                               isinstance(description, (str, type(None))) and
                               isinstance(note, (str, type(None))) and
                               isinstance(buy_date, (datetime.datetime, type(None))))

        if is_correct_instance and not (receipt_id is None) and RS.find_receipt(session, receipt_id) is not None:
            equipment = Model(price, model, buy_date, receipt_id, description, note)
            session.add(equipment)
            session.commit()
            return True
        elif isinstance(equipment, Model):
            session.add(equipment)
            session.commit()
            return True

        return False

    # Delete equipment return True if successful
    @staticmethod
    def delete_equipment(session, equ_id):
        equipment = EquipmentService.find_equipment(session, equ_id)
        if equipment is None:
            return False

        session.add(equipment)
        session.commit()
        return True

    # Get a list of all equipment
    @staticmethod
    def get_all_equipment(session):
        return session.query(Model)

    # Find equipment from id
    @staticmethod
    def find_equipment(session, equ_id):
        return session.query(Model).filter_by(id=equ_id).first()

    # Update fields
    @staticmethod
    def update_fields(session, equ_id, fields_values):
        for (f, v) in fields_values:
            EquipmentService.__update_field(session, equ_id, f, v)

    # Private method used in class to update specific field
    @staticmethod
    def __update_field(session, equ_id, field, value):
        session.query(Model).filter_by(id=equ_id).update({field: value})
        session.commit()
