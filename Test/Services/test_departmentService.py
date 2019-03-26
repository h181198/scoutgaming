from unittest import TestCase
from Services.DepartmentService import DepartmentService as DS
from Models.Department import Department
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database = create_engine('postgres://localhost:5432/myDatabase')
database.connect()

Session = sessionmaker(database)
session = Session()


class TestDepartmentService(TestCase):

    def test_add_department(self):
        self.assertTrue(DS.add_department(session, "Norway", "Bergen"))
        department = DS.find_department(session, 1)
        self.assertTrue(department.country == "Norway")

        d = Department(country="Denmark", unit="Copenhagen")
        self.assertTrue(DS.add_department(session=session, department=d))
        department = DS.find_department(session, 2)
        self.assertTrue(department.country == "Denmark")

        self.assertFalse(DS.add_department(session))
        self.assertFalse(DS.add_department(session=session, department="string"))
        self.assertFalse(DS.add_department(session=session, unit=1))
        self.assertFalse(DS.add_department(session=session, unit="string"))
        self.assertFalse(DS.add_department(session=session, country=1))
        self.assertFalse(DS.add_department(session=session, country="string"))
        self.assertFalse(DS.add_department(session=session, country=1, unit=1))
        self.assertFalse(DS.add_department(session=session, country="string", unit=1))
        self.assertFalse(DS.add_department(session=session, country=1, unit="string"))

    def test_delete_department(self):
        self.assertIsNone(DS.find_department(session, 120931))
        DS.delete_department(session, 2)
        self.assertIsNone(DS.find_department(session, 2))

    def test_get_all_departments(self):
        d = Department(country="Russia", unit="Moscow")
        DS.add_department(session=session, department=d)
        departments_list = DS.get_all_departments(session)
        self.assertEqual(d, departments_list.all().pop())

    def test_find_department(self):
        department = Department(country="Sweden", unit="Stockholm")
        DS.add_department(session=session, department=department)
        self.assertEqual(department, DS.find_department(session, department.id))
        self.assertEqual(None, DS.find_department(session, 0))
