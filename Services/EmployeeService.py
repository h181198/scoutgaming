from Models.Department import Department
from Models.Employee import Employee as Model


# Add employee return True if successful, start_date is optional
def add_employee(name, department_id, session, start_date=None):
    if start_date is None:
        employee = Model(name=name, department_id=department_id)
    else:
        # Try not to use
        employee = Model(name=name, department_id=department_id, start_date=start_date)

    department = session.query(Department).filter_by(id=department_id).first()

    if employee is None or name is None or department is None:
        return False

    session.add(employee)
    session.commit()
    return True


# Delete employee return true if successful
def delete_employee(emp_id, session):
    employee = find_employee(emp_id, session)

    if employee is None:
        return False

    session.delete(employee)
    session.commit()
    return True


# Get a list of all employees
def get_all_employees(session):
    return session.query(Model)


# Find an employee from id
def find_employee(emp_id, session):
    return session.query(Model).filter_by(id=emp_id).first()
