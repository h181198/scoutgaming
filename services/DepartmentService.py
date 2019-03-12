from Services.ConnectionService import database, create_session

import Models.Department as Model

# Add a new department
def add_department(country, unit):
    department = Model.Department(country=country, unit=unit)
    session = create_session()

    session.add(department)
    session.commit()


# Remove department based on id
def delete_department(id):
    session = create_session()

    department = find_department(id)
    session.delete(department)
    session.commit()


# Get a list of all departments
def get_all_departments():
    return create_session().query(Model.Department)


# Get one department from id
def find_department(id):
    return create_session().query(Model.Department).filter_by(id=id).first()
