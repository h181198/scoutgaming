from Services.DepartmentService import DepartmentService as DS
from Models.Employee import Employee as Model
import datetime


class EmployeeService:
    # Add employee return True if successful
    @staticmethod
    def add_employee(session, employee_id=None, name=None, department_id=None, start_date=None, employee=None):
        is_correct_instance = (isinstance(name, str) and isinstance(department_id, int) and
                               isinstance(employee_id, str) and isinstance(start_date, (datetime.datetime, type(None))))

        if start_date is not None and employee is None and is_correct_instance:
            employee = Model(id=employee_id, name=name, department_id=department_id, start_date=start_date)
        elif employee is None and is_correct_instance:
            employee = Model(id=employee_id, name=name, department_id=department_id)
        if isinstance(employee, Model) and DS.find_department(session, employee.department_id) is not None:
            session.add(employee)
            session.commit()
            return True

        return False

    # Update employee values
    @staticmethod
    def update_employee(session, emp_id, name, department_id, start_date, end_date):
        employee = EmployeeService.find_employee(session, emp_id)
        if isinstance(name, str):
            employee.name = name
        if isinstance(department_id, int):
            employee.department_id = department_id
        if not isinstance(start_date, str):
            employee.start_date = start_date
        if not isinstance(end_date, str):
            employee.end_date = end_date

        session.commit()

    # Delete employee return true if successful
    @staticmethod
    def delete_employee(session, emp_id):
        employee = EmployeeService.find_employee(session, emp_id)
        if employee is None:
            return False

        session.delete(employee)
        session.commit()
        return True

    # Get a list of all employees
    @staticmethod
    def get_all_employees(session):
        return session.query(Model)

    # Find an employee from id
    @staticmethod
    def find_employee(session, emp_id):
        return session.query(Model).filter_by(id=emp_id).first()

    # Add date they quit or got fired
    @staticmethod
    def add_end_date(session, employee_id, end_date=None):
        if end_date is None or not isinstance(end_date, datetime.datetime):
            end_date = datetime.datetime.now()

        session.query(Model).filter_by(id=employee_id).update({"end_date": end_date.strftime("%x")})
        session.commit()
