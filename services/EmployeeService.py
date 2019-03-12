from Services.ConnectionService import create_session
from sqlalchemy.types import DateTime

import Models.Employee as Model


# Add employee
def add_employee(name, department_id, start_date):
    if start_date is None:
        start_date = DateTime()

    session = create_session()

    employee = Model.Employee(name=name, department_id=department_id, start_date=start_date)
    session.add(employee)

    session.commit()


# Delete employee
def delete_employee(id):
    session = create_session()

    employee = find_employee(id)
    session.delete(employee)

    session.commit()


# Get a list of all employees
def get_all_employees():
    return create_session().query(Model.Employee)


# Find an employee from id
def find_employee(id):
    return create_session().query(Model.Employee).filter_by(id=id).first()
