from Services.ConnectionService import create_session
from Models.Department import Department as Model


# Add a new department return True if successful
def add_department(country, unit):
    if (country is None) or (unit is None):
        return False
    else:
        department = Model(country=country, unit=unit)
        session = create_session()

        session.add(department)
        session.commit()
        return True


# Remove department based on id return True if successful
def delete_department(dep_id):
    session = create_session()

    department = find_department(dep_id)

    if department is None:
        return False
    else:
        session.delete(department)
        session.commit()
        return True


# Get a list of all departments
def get_all_departments():
    return create_session().query(Model)


# Get one department from id
def find_department(dep_id):
    return create_session().query(Model).filter_by(id=dep_id).first()
