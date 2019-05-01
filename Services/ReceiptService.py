from Models.Receipt import Receipt as Model
from Helpers.ServiceHelper import secure_text
import json


class ReceiptService:
    # Add a receipt return receipt if successful
    @staticmethod
    def add_receipt(session, supplement=None, year=None, receipt=None):
        is_none = supplement is None or year is None
        is_correct_instance = isinstance(supplement, str) and isinstance(year, int)

        if not is_none and is_correct_instance:
            receipt_id = str(year) + supplement
            receipt = Model(comb_id=receipt_id, supplement=supplement, year=year)
            session.add(receipt)
            session.commit()
            return receipt
        elif isinstance(receipt, Model):
            session.add(receipt)
            session.commit()
            return receipt

        return None

    # Update receipt in database
    @staticmethod
    def update_receipt(session, rec_id, supplement, year):
        receipt = ReceiptService.find_receipt(session, rec_id)
        receipt.supplement = supplement
        if isinstance(year, int):
            receipt.year = year
            receipt.comb_id = str(year) + supplement
        session.commit()

    # Get a list of all receipts
    @staticmethod
    def get_all_receipts(session):
        return session.query(Model)

    # Get a list of all receipts as json
    @staticmethod
    def get_all_receipts_json(session):
        data = ReceiptService.get_all_receipts(session)
        result = "["
        for rec in data:
            result += ReceiptService.get_receipt_json(session, rec.id) + ","

        return result[:len(result)-1] + "]"

    # Get receipt as json
    @staticmethod
    def get_receipt_json(session, rec_id):
        receipt = ReceiptService.find_receipt(session, rec_id)
        result_json = {
            'id': receipt.id,
            'comb_id': receipt.comb_id,
            'year': receipt.year,
            'supplement': secure_text(receipt.supplement)
        }
        return json.dumps(result_json, indent=4, sort_keys=False, default=str)

    # Find receipt from id
    @staticmethod
    def find_receipt(session, rec_id):
        if isinstance(rec_id, int):
            return session.query(Model).filter_by(id=rec_id).first()
        return None
