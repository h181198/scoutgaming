from Models.Receipt import Receipt as Model
import json


class ReceiptService:
    # Add a receipt return receipt if successful
    @staticmethod
    def add_receipt(session, supplement=None, year=None, receipt=None):
        is_none = supplement is None or year is None
        is_correct_instance = isinstance(supplement, str) and isinstance(year, int)

        if not is_none and is_correct_instance:
            receipt_id = supplement + str(year)
            receipt = Model(id=receipt_id, supplement=supplement, year=year)
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
            receipt.id = supplement + str(year)
        session.commit()

    # Get a list of all receipts
    @staticmethod
    def get_all_receipts(session):
        return session.query(Model)

    # Get a list of all receipts as json
    @staticmethod
    def get_all_receipts_json(database):
        data = database.execute("SELECT * FROM receipts")
        return json.dumps([dict(r) for r in data])

    # Find receipt from id
    @staticmethod
    def find_receipt(session, rec_id):
        if isinstance(rec_id, str):
            return session.query(Model).filter_by(id=rec_id).first()
        return None
