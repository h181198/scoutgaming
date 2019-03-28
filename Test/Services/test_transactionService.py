from unittest import TestCase

from Services.TransactionService import TransactionService as TS
from Services.DepartmentService import DepartmentService as DS
from Services.EquipmentService import EquipmentService as EqS
from Services.EmployeeService import EmployeeService as EmS
from Services.ReceiptService import ReceiptService as RS

from Models.Transaction import Transaction
from Models.Department import Department
from Models.Equipment import Equipment
from Models.Employee import Employee
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

default_eq = Equipment(id=1, price=22000, model="Skjerm", buy_date=date,
                  receipt_id="ID", description="Solid work", note="Do not drop")
EqS.add_equipment(session=session, equipment=default_eq)

default_dep = Department(id=1, country="Norway", unit="Bergen")
DS.add_department(session=session, department=default_dep)

default_emp = Employee(id="E1", name="Smiedth", department_id=default_dep.id)
EmS.add_employee(session=session, employee=default_emp)

default_emp2 = Employee(id="E4", name="Jon", department_id=default_dep.id)
EmS.add_employee(session=session, employee=default_emp2)


class TestTransactionService(TestCase):
    def test_add_transaction(self):
        trans = Transaction(employee_id="E1", equipment_id=1)
        self.assertTrue(TS.add_transaction(session=session, transaction=trans))
        self.assertTrue(TS.add_transaction(session=session, employee_id="E1", equipment_id=1))
        self.assertFalse(TS.add_transaction(session=session, employee_id=0, equipment_id=1))

    def test_update_transaction(self):
        trans = Transaction(id=10, employee_id="E1", equipment_id=1)
        TS.add_transaction(session=session, transaction=trans)
        self.assertEqual(trans, TS.find_transaction(session, 10))
        TS.update_transaction(session, 10, 1, "E4")
        self.assertNotEqual("E1", TS.find_transaction(session, 10).employee_id)

    def test_get_all_transactions(self):
        trans = Transaction(id=40, employee_id="E4", equipment_id=1)
        TS.add_transaction(session=session, transaction=trans)
        trans_list = TS.get_all_transactions(session)
        self.assertEqual(trans, trans_list.all().pop())
