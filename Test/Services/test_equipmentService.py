from unittest import TestCase
from Services.EquipmentService import EquipmentService as EqS
from Services.ReceiptService import ReceiptService as RS
from Models.Equipment import Equipment
from Models.Receipt import Receipt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

database = create_engine('postgres://localhost:5432/myDatabase')
database.connect()

now = datetime.datetime.now()
date = now.strftime("%Y") + "-" + now.strftime("%m") + "-" + now.strftime("%d")

Session = sessionmaker(database)
session = Session()

default_rec = Receipt(id="ID", supplement="IDK", year=2020)
RS.add_receipt(session=session, receipt=default_rec)


class TestEquipmentService(TestCase):
    def test_add_equipment(self):
        equipment = Equipment(price=4800, model="Macbook 12", receipt_id="ID")
        self.assertTrue(EqS.add_equipment(session=session, equipment=equipment))
        self.assertTrue(EqS.add_equipment(session=session, price=23000, receipt_id="ID"))

        self.assertFalse(EqS.add_equipment(session=session, model="Acer Predator"))
        self.assertFalse(EqS.add_equipment(session=session, buy_date=date))
        self.assertFalse(EqS.add_equipment(session=session, receipt_id="ID" ))
        self.assertFalse(EqS.add_equipment(session=session, description="Solid work"))
        self.assertFalse(EqS.add_equipment(session=session, note="Do not drop"))

        self.assertTrue(EqS.add_equipment(session=session, price=23000, receipt_id="ID", model="Acer Predator"))
        self.assertTrue(EqS.add_equipment(session=session, price=23000, receipt_id="ID", buy_date=date))
        self.assertTrue(EqS.add_equipment(session=session, price=23000, receipt_id=None))
        self.assertTrue(EqS.add_equipment(session=session, price=23000, receipt_id="ID", description="Solid work"))
        self.assertTrue(EqS.add_equipment(session=session, price=23000, receipt_id="ID", note="Do not drop"))

        self.assertTrue(EqS.add_equipment(session=session, price=22000, model="Acer Predator", buy_date=date,
                                          receipt_id="ID", description="Solid work", note="Do not drop"))
        self.assertFalse(EqS.add_equipment(session=session, price="22", model=12, buy_date="i dag",
                                           receipt_id=5, description=13, note=14))

    def test_get_all_equipment(self):
        eq = Equipment(price=22, model="Poteter", receipt_id="ID")
        EqS.add_equipment(session=session, equipment=eq)
        eq_list = EqS.get_all_equipment(session)
        self.assertEqual(eq, eq_list.all().pop())

    def test_find_equipment(self):
        eq = Equipment(id=20, price=22, model="Gulrot", receipt_id="ID")
        EqS.add_equipment(session=session, equipment=eq)
        self.assertEqual(eq, EqS.find_equipment(session, 20))
        self.assertIsNone(EqS.find_equipment(session, 0))

    def test_update_equipment(self):
        eq = Equipment(id=22, price=22, model="Vannmelon", receipt_id="ID")
        EqS.add_equipment(session=session, equipment=eq)
        self.assertEqual(eq, EqS.find_equipment(session, 22))
        EqS.update_equipment(session=session, equ_id=22, price=40, model="wat", buy_date=date,
                             receipt_id="None", description="None", note="None")
        self.assertNotEqual("Vannmelon", EqS.find_equipment(session, 22).model)
