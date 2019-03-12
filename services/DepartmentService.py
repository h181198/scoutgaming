from Models.Department import Department
from sqlalchemy.orm import sessionmaker
from Services.ConnectionService import database


# Add a new department
def add_department(country, unit):
    department = Department(country=country, unit=unit)
    Session = sessionmaker(database)
    session = Session()

    session.add(department)
    session.commit()


# Remove department based on id
def delete_department(id):
    Session = sessionmaker(database)
    session = Session()

    department = session.query(Department).filter_by(id=id).first()
    session.delete(department)
    session.commit()


# Get a list of all departments
def get_all_departments():
    Session = sessionmaker(database)
    session = Session()

    return session.query(Department)
