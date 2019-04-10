from Services.DepartmentService import DepartmentService as DS
from Models.Employee import Employee as Model
import datetime
import json


class EmployeeService:
    # Add employee return True if successful
    @staticmethod
    def add_employee(session, employee_number=None, name=None, department_id=None, start_date=None, end_date=None,
                    employee=None):
        is_correct_instance = (isinstance(name, str) and isinstance(department_id, int) and
                               isinstance(employee_number, str) and isinstance(start_date, (str, type(None)))
                               and isinstance(end_date, (str, type(None))))

        if start_date is not None and start_date != '' and employee is None and is_correct_instance and end_date != '':
            employee = Model(employee_number=employee_number, name=name, department_id=department_id,
                             start_date=start_date, end_date=end_date)
        elif end_date == '' and is_correct_instance:
            employee = Model(employee_number=employee_number, name=name, department_id=department_id,
                             start_date=start_date)
        elif employee is None and is_correct_instance:
            employee = Model(employee_number=employee_number, name=name, department_id=department_id)
        if isinstance(employee, Model) and DS.find_department(session, employee.department_id) is not None:
            session.add(employee)
            session.commit()
            return True

        return False

    # Update employee values
    @staticmethod
    def update_employee(session, emp_id, emp_number, name, department_id, start_date, end_date):
        employee = EmployeeService.find_employee(session, emp_id)
        if isinstance(emp_number, str) and emp_number != '':
            employee.employee_number = emp_number
        if isinstance(name, str):
            employee.name = name
        if isinstance(department_id, (int, type(None))):
            employee.department_id = department_id
        if start_date != "None" and start_date != "":
            employee.start_date = start_date
        if end_date != "None" and end_date != "":
            employee.end_date = end_date

        session.commit()

    # Get a list of all employees
    @staticmethod
    def get_all_employees(session):
        return session.query(Model)

    # Get a list of all employees as json
    @staticmethod
    def get_all_employees_json(database):
        data = database.execute("SELECT * FROM employees")
        return json.dumps([dict(r) for r in data])

    @staticmethod
    def get_employee_json(session, emp_id):
        emp = EmployeeService.find_employee(session, int(emp_id))
        department_unit = DS.find_department(session, emp.department_id).unit
        my_json = {
            'id': emp.id,
            'employee_number': emp.employee_number,
            'name': emp.name,
            'department_id': department_unit,
            'start_date': emp.start_date,
            'end_date': emp.end_date
        }
        return json.dumps(my_json, indent=4, sort_keys=False, default=str)

    # Find an employee from id
    @staticmethod
    def find_employee(session, emp_id):
        if isinstance(emp_id, int):
            return session.query(Model).filter_by(id=emp_id).first()
        return None

    # Add date they quit or got fired
    @staticmethod
    def add_end_date(session, employee_id, end_date=None):
        if end_date is None or not isinstance(end_date, datetime.datetime):
            now = datetime.datetime.now()
            end_date = now.strftime("%Y") + "-" + now.strftime("%m") + "-" + now.strftime("%d")

        session.query(Model).filter_by(id=employee_id).update({"end_date": end_date.strftime("%x")})
        session.commit()
