from Models.Department import Department as Model
from Helpers.ServiceHelper import secure_text
import json


class DepartmentService:
    # Add a new department return department if successful
    @staticmethod
    def add_department(session, country=None, unit=None, department=None):
        is_string = isinstance(unit, str) and isinstance(country, str)
        is_none = country is None or unit is None or (unit == "" and country == "")

        if not is_none and is_string:
            department = Model(country=country, unit=unit)
            session.add(department)
            session.commit()
            return department
        elif isinstance(department, Model):
            session.add(department)
            session.commit()
            return department

        return None

    # Update the department in the database
    @staticmethod
    def update_department(session, dep_id, country, unit):
        department = DepartmentService.find_department(session, dep_id)
        if country != "":
            department.country = country
        if unit != "":
            department.unit = unit
        session.commit()

    # Get a list of all departments
    @staticmethod
    def get_all_departments(session):
        return session.query(Model)

    # Get department ass json
    @staticmethod
    def get_department_json(session, dep_id):
        department = DepartmentService.find_department(session, dep_id)

        my_json = {
            'id': department.id,
            'display_id': department.id,
            'country': secure_text(department.country),
            'unit': secure_text(department.unit)
        }
        return json.dumps(my_json, indent=4, sort_keys=False, default=str)

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
