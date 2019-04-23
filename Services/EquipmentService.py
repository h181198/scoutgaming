from Models.Equipment import Equipment as Model
from Services.ReceiptService import ReceiptService as RS
import json


class EquipmentService:
    # Add new equipment, return equipment if successful
    @staticmethod
    def add_equipment(session, price=None, currency=None, model=None, buy_date=None, receipt_id=None,
                      description=None, note=None, equipment=None):
        is_correct_instance = (isinstance(price, int) and
                               isinstance(currency, (str, type(None))) and
                               isinstance(model, (str, type(None))) and
                               isinstance(receipt_id, (str, type(None))) and
                               isinstance(description, (str, type(None))) and
                               isinstance(note, (str, type(None))) and
                               isinstance(buy_date, (str, type(None))))

        if is_correct_instance and (receipt_id is None or RS.find_receipt(session, receipt_id) is not None):
            equipment = Model(price=price, currency=currency, model=model, buy_date=buy_date, receipt_id=receipt_id,
                              description=description, note=note)
            session.add(equipment)
            session.commit()
            return equipment
        elif isinstance(equipment, Model):
            session.add(equipment)
            session.commit()
            return equipment

        return None

    # Update equipment
    @staticmethod
    def update_equipment(session, equ_id, price, currency, model, buy_date, receipt_id, description, note):
        equipment = EquipmentService.find_equipment(session, equ_id)
        if isinstance(price, int):
            equipment.price = price
        if currency != "None":
            equipment.currency = currency
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
    def get_all_equipments(session):
        return session.query(Model)

    # Get a list of all equipment as json
    @staticmethod
    def get_all_equipments_json(session):
        data = EquipmentService.get_all_equipments(session)
        result_json = "["
        for eq in data:
            eq_json = EquipmentService.get_equipment_json(session, eq.id)
            result_json += eq_json + ","

        return result_json[:len(result_json)-1] + "]"

    # Get an equipment as json
    @staticmethod
    def get_equipment_json(session, emp_id):
        eq = EquipmentService.find_equipment(session, int(emp_id))
        my_json = {
            'id': eq.id,
            'price': eq.price,
            'currency': eq.currency,
            'model': eq.model,
            'buy_date': eq.buy_date,
            'receipt_id': eq.receipt_id,
            'description': eq.description,
            'note': eq.note
        }
        return json.dumps(my_json, indent=4, sort_keys=False, default=str)

    # Find equipment from id
    @staticmethod
    def find_equipment(session, equ_id):
        if isinstance(equ_id, int):
            return session.query(Model).filter_by(id=equ_id).first()
        return None

    # Find equipment with None values
    @staticmethod
    def find_missing(session):
        equ_list = EquipmentService.get_all_equipments(session)
        has_missing = []
        for equ in equ_list:
            if equ.model is None or equ.buy_date is None or equ.receipt_id is None:
                has_missing.append(equ)

        return has_missing

