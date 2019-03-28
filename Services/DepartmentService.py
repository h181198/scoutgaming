from Models.Department import Department as Model
import json


class DepartmentService:
    # Add a new department return True if successful
    @staticmethod
    def add_department(session, country=None, unit=None, department=None):
        is_string = isinstance(unit, str) and isinstance(country, str)
        is_none = country is None or unit is None

        if not is_none and is_string:
            department = Model(country=country, unit=unit)
            session.add(department)
            session.commit()
            return True
        elif isinstance(department, Model):
            session.add(department)
            session.commit()
            return True

        return False

    # Update the department in the database
    @staticmethod
    def update_department(session, dep_id, country, unit):
        department = DepartmentService.find_department(session, dep_id)
        department.country = country
        department.unit = unit
        session.commit()

    # Get a list of all departments
    @staticmethod
    def get_all_departments(session):
        return session.query(Model)

    # Get list of all departments as objects
    @staticmethod
    def get_all_departments_json(database):
        data = database.execute("SELECT * FROM departments")
        return json.dumps([dict(r) for r in data])

    # Get one department from id or unit
    @staticmethod
    def find_department(session, dep_id=None, unit=None):
        if unit is None:
            return session.query(Model).filter_by(id=dep_id).first()
        if isinstance(dep_id, int):
            return session.query(Model).filter_by(unit=unit).first()

        return None
