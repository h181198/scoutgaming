from Models.Receipt import Receipt as Model


class ReceiptService:
    # Add a receipt return True if successful
    @staticmethod
    def add_receipt(session, supplement=None, year=None, receipt=None):
        is_none = supplement is None or year is None
        is_correct_instance = isinstance(supplement, str) and isinstance(year, int)

        if not is_none and is_correct_instance:
            receipt_id = supplement + str(year)
            receipt = Model(id=receipt_id, supplement=supplement, year=year)
            session.add(receipt)
            session.commit()
            return True
        elif isinstance(receipt, Model):
            session.add(receipt)
            session.commit()
            return True

        return False

    # Update receipt in database
    @staticmethod
    def update_receipt(session, rec_id, supplement, year):
        receipt = ReceiptService.find_receipt(session, rec_id)
        receipt.supplement = supplement
        if isinstance(year, int):
            receipt.year = year
        session.commit()

    # Delete a receipt return True if successful
    @staticmethod
    def delete_receipt(session, rec_id):
        receipt = ReceiptService.find_receipt(session, rec_id)

        if receipt is None:
            return False

        session.delete(receipt)
        session.commit()
        return True

    # Get a list of all receipts
    @staticmethod
    def get_all_receipts(session):
        return session.query(Model)

    # Find receipt from id
    @staticmethod
    def find_receipt(session, rec_id):
        if isinstance(rec_id, str):
            return session.query(Model).filter_by(id=rec_id).first()
        return None
