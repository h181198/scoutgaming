from flask import Flask
from flask_admin import Admin
from sqlalchemy import create_engine


app = Flask(__name__)
database = create_engine('postgres://localhost:5432/myDatabase')
database.connect()


@app.route('/')
def hello_world():
    return 'Hello World!'


admin = Admin(app)

if __name__ == '__main__':

    app.run(debug=True)
