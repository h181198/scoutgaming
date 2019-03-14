from Models.Department import Department as Model


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

    # Remove department based on id return True if successful
    @staticmethod
    def delete_department(session, dep_id):
        department = DepartmentService.find_department(session, dep_id)

        if department is None:
            return False
        else:
            session.delete(department)
            session.commit()
            return True

    # Get a list of all departments
    @staticmethod
    def get_all_departments(session):
        return session.query(Model)

    # Get one department from id
    @staticmethod
    def find_department(session, dep_id):
        return session.query(Model).filter_by(id=dep_id).first()
