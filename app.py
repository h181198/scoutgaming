from flask import Flask
from flask_admin import Admin
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Models.Department import Department


app = Flask(__name__)
database = create_engine('postgres://localhost:5432/myDatabase')
database.connect()

Base = declarative_base()

Session = sessionmaker(database)
session = Session()

# Comment in if you want it to create the database for you
# Base.metadata.create_all(database)

test_department = Department(country="Norway", unit="Oslo")
session.add(test_department)
session.commit()

myList = session.query(Department)

for a in myList:
    print(type(a))


@app.route('/')
def hello_world():
    return 'Hello World!'


admin = Admin(app)

if __name__ == '__main__':
    app.run(debug=True)
