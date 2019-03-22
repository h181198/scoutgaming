from flask import Flask, render_template, redirect, url_for, request
from flask_admin import Admin
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models.Employee import Employee


app = Flask(__name__)

database = create_engine('postgres://postgres:admin@localhost:5432/mydatabase')
database.connect()

admin = Admin(app)

app.config['SECRET_KEY'] = 'lameKey'

Session = sessionmaker(database)
session = Session()


@app.route('/')
def index():
    return render_template('Views/index.html')


@app.route('/employee')
def employee():
    data = session.query(Employee)
    return render_template('Views/Employee/index.html', data=data)


@app.route('/employee/delete/<int:postID>', methods=['POST'])
def delete_employee(postID):
    print(postID)
    return redirect(url_for('employee'))


@app.route('/employee/edit/<int:empID>')
def edit_employee(empID):
    empID = str(empID)
    person = session.query(Employee).get(empID)
    print(person.start_date)
    return render_template('Views/Employee/edit.html', data=person)


@app.route('/equipment')
def equipment():
    return render_template('Views/Equipment/index.html')


@app.route('/receipt')
def receipt():
    return render_template('Views/Receipt/index.html')


@app.route('/transaction')
def transaction():
    return render_template('Views/Transaction/index.html')


@app.route('/department')
def department():
    return render_template('Views/Department/index.html')


if __name__ == '__main__':
    app.run(debug=True)
