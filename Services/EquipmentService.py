from Models.Equipment import Equipment as Model
from Services.ReceiptService import ReceiptService as RS
from Services.TransactionService import TransactionService as TS


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
                               isinstance(buy_date, (str, type(None))))

        if is_correct_instance and (receipt_id is None or RS.find_receipt(session, receipt_id) is not None):
            equipment = Model(price=price, model=model, buy_date=buy_date, receipt_id=receipt_id,
                              description=description, note=note)
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

        # Find all transactions for that equipment and delete them
        # No use in keeping transactions without equipment
        transaction_list = TS.get_all_transactions(session)
        for trans in transaction_list:
            if trans.equipment_id == equ_id:
                TS.delete_transaction(session, trans.id)

        session.delete(equipment)
        session.commit()
        return True

    # Update equipment
    @staticmethod
    def update_equipment(session, equ_id, price, model, buy_date, receipt_id, description, note):
        equipment = EquipmentService.find_equipment(session, equ_id)
        if isinstance(price, int):
            equipment.price = price
        if model != "None":
            equipment.model = model
        if buy_date != "None":
            equipment.buy_date = buy_date
        if receipt_id != "None":
            equipment.receipt_id = receipt_id
        if description != "None":
            equipment.description = description
        if note != "None":
            equipment.note = note

        session.commit()

    # Get a list of all equipment
    @staticmethod
    def get_all_equipment(session):
        return session.query(Model)

    # Find equipment from id
    @staticmethod
    def find_equipment(session, equ_id):
        if isinstance(equ_id, int):
            return session.query(Model).filter_by(id=equ_id).first()
        return None
