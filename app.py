from flask import Flask
from flask_admin import Admin, BaseView, expose
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_admin.contrib.sqla import ModelView
from Models.Department import Department
from Models.Employee import Employee


app = Flask(__name__)
database = create_engine('postgres://postgres:admin@localhost:5432/mydatabase')
database.connect()

Session = sessionmaker(database)
session = Session()

admin = Admin(app)
admin.add_view(ModelView(Department, session))
admin.add_view(ModelView())

if __name__ == '__main__':
    app.run(debug=True)
