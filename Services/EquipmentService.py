from Models.Equipment import Equipment as Model
from Services.ReceiptService import ReceiptService as RS
from Helpers.ServiceHelper import secure_text
import json
import datetime


class EquipmentService:
    # Add new equipment, return equipment if successful
    @staticmethod
    def add_equipment(session, price=None, currency=None, model=None, buy_date=None, receipt_id=None,
                      description=None, note=None, equipment=None):
        is_correct_instance = (isinstance(price, int) and
                               isinstance(currency, (str, type(None))) and
                               isinstance(model, (str, type(None))) and
                               isinstance(receipt_id, (int, type(None))) and
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
        if receipt_id != "None" and isinstance(receipt_id, (int, type(None))):
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
        curr_rec = RS.find_receipt(session, eq.receipt_id)
        rec_id = None
        if curr_rec is not None:
            rec_id = curr_rec.comb_id

        my_json = {
            'id': eq.id,
            'price': eq.price,
            'currency': secure_text(eq.currency),
            'model': secure_text(eq.model),
            'buy_date': eq.buy_date,
            'receipt_id': rec_id,
            'description': secure_text(eq.description),
            'note': secure_text(eq.note)
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

    # Find amount of money each month in the last year
    @staticmethod
    def money_spent(session):
        equipment_list = EquipmentService.get_all_equipments(session)
        bought_last_year = []
        current_date = datetime.datetime.now().date()
        interval = datetime.timedelta(days=-365)
        for equ in equipment_list:
            if (equ.buy_date - current_date) <= interval:
                bought_last_year.append(equ)

        # place in a dict for the month, create private method for that
        return EquipmentService.__create_dict(bought_last_year)

    # Creates a dict for the month and the value spent
    @staticmethod
    def __create_dict(equ_list):
        nok_result = dict()
        uah_result = dict()
        current_date = datetime.datetime.now().date()
        for equ in equ_list:
            month = equ.buy_date.strftime("%m")
            year = equ.buy_date.strftime("%y")
            same_month = (month == current_date.strftime("%m")) and (year != current_date.strftime("%y"))

            if not same_month and equ.currency == "NOK":
                nok_result[month] += equ.price
            elif not same_month and equ.currency == "UAH":
                uah_result[month] += equ.price

        return {nok_result, uah_result}
