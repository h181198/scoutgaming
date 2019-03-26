from unittest import TestCase
from Services.ReceiptService import ReceiptService as RS
from Models.Receipt import Receipt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database = create_engine('postgres://localhost:5432/myDatabase')
database.connect()

Session = sessionmaker(database)
session = Session()


class TestReceiptService(TestCase):
    def test_add_receipt(self):
        self.assertTrue(RS.add_receipt(session, "UEBoom", 2012))
        receipt = RS.find_receipt(session, "UEBoom2012")
        self.assertEqual(receipt.year, 2012)

        r = Receipt(id="Fac12", supplement="Fac", year=12)
        self.assertTrue(RS.add_receipt(session=session, receipt=r))
        receipt = RS.find_receipt(session, r.id)
        self.assertEqual(r, receipt)

        self.assertFalse(RS.add_receipt(session))
        self.assertFalse(RS.add_receipt(session=session, receipt="string"))
        self.assertFalse(RS.add_receipt(session=session, supplement="string"))
        self.assertFalse(RS.add_receipt(session=session, supplement=1))
        self.assertFalse(RS.add_receipt(session=session, year=""))
        self.assertFalse(RS.add_receipt(session=session, year=2))
        self.assertFalse(RS.add_receipt(session=session, supplement=1, year="string"))
        self.assertFalse(RS.add_receipt(session=session, supplement=1, year=1))
        self.assertFalse(RS.add_receipt(session=session, supplement="string", year="string"))

    def test_delete_receipt(self):
        self.assertIsNone(RS.find_receipt(session, "UA20"))
        RS.add_receipt(session, "UA", 20)
        self.assertTrue(RS.find_receipt(session, "UA20").year == 20)
        RS.delete_receipt(session, "UA20")
        self.assertIsNone(RS.find_receipt(session, "UA20"))

    def test_get_all_receipts(self):
        r = Receipt(id="WW12", supplement="WW", year=12)
        RS.add_receipt(session=session, receipt=r)
        receipts_list = RS.get_all_receipts(session)
        self.assertEqual(r, receipts_list.all().pop())

    def test_find_receipt(self):
        r = Receipt(id="Sweden2019", supplement="Sweden", year=2019)
        RS.add_receipt(session=session, receipt=r)
        self.assertEqual(r, RS.find_receipt(session, r.id))
        self.assertEqual(None, RS.find_receipt(session, "0"))
