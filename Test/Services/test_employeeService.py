from unittest import TestCase
from Services.EmployeeService import EmployeeService as EmS
from Services.DepartmentService import DepartmentService as DS
from Models.Employee import Employee
from Models.Department import Department
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
import datetime

database = create_engine('postgres://localhost:5432/myDatabase')
database.connect()

today = datetime.datetime.now()

Session = sessionmaker(database)
session = Session()
default_dep = Department(country="Norway", unit="Bergen")
DS.add_department(session=session, department=default_dep)


class TestEmployeeService(TestCase):
    def test_add_employee(self):
        emp = Employee(id="E1", name="Smiedth", department_id=default_dep.id)
        self.assertTrue(EmS.add_employee(session=session, employee=emp))
        self.assertTrue(EmS.add_employee(session=session, employee_id="E2", name="Juaon",
                                         department_id=default_dep.id))

        self.assertTrue(EmS.add_employee(session=session, employee_id="E3", name="Shinna",
                                         department_id=default_dep.id, start_date=today))

        self.assertFalse(EmS.add_employee(session))
        self.assertFalse(EmS.add_employee(session=session, employee_id=1))
        self.assertFalse(EmS.add_employee(session=session, employee_id="E4"))
        self.assertFalse(EmS.add_employee(session=session, name=1))
        self.assertFalse(EmS.add_employee(session=session, name="string"))
        self.assertFalse(EmS.add_employee(session=session, department_id=1))
        self.assertFalse(EmS.add_employee(session=session, department_id="1"))
        self.assertFalse(EmS.add_employee(session=session, start_date=1))
        self.assertFalse(EmS.add_employee(session=session, start_date="string"))
        self.assertFalse(EmS.add_employee(session=session, employee="Hello"))
        self.assertFalse(EmS.add_employee(session=session, employee_id=1, name=1, department_id=1, start_date=1))
        self.assertFalse(EmS.add_employee(session=session, employee_id="E4", name=1, department_id=1, start_date=1))
        self.assertFalse(EmS.add_employee(session=session, employee_id=1, name="Jonatan", department_id=1, start_date=1))
        self.assertFalse(EmS.add_employee(session=session, employee_id=1, name=1,
                                          department_id=default_dep.id, start_date=1))
        self.assertFalse(EmS.add_employee(session=session, employee_id=1, name=1,
                                          department_id=1, start_date=func.now()))

    def test_delete_employee(self):
        self.assertIsNone(EmS.find_employee(session, "E5"))
        EmS.add_employee(session=session, employee_id="E5", name="Jon", department_id=default_dep.id)
        self.assertEqual(EmS.find_employee(session, "E5").name, "Jon")
        EmS.delete_employee(session, "E5")
        self.assertIsNone(EmS.find_employee(session, "E5"))

    def test_get_all_employees(self):
        e = Employee(id="E6", name="testre", department_id=default_dep.id)
        EmS.add_employee(session=session, employee=e)
        employees_list = EmS.get_all_employees(session)
        self.assertEqual(e, employees_list.all().pop())

    def test_find_employee(self):
        e = Employee(id="E7", name="test", department_id=default_dep.id)
        EmS.add_employee(session=session, employee=e)
        self.assertEqual(e, EmS.find_employee(session, e.id))
        self.assertEqual(None, EmS.find_employee(session, "0"))

    def test_add_end_date(self):
        e = Employee(id="E8", name="test quit", department_id=default_dep.id)
        EmS.add_employee(session=session, employee=e)
        self.assertTrue(EmS.find_employee(session, e.id).end_date is None)
        EmS.add_end_date(session, e.id, today)
        self.assertEqual(today, EmS.find_employee(session, e.id).end_date)
