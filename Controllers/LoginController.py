from flask import Blueprint, redirect, request, flash, url_for, render_template
from flask_login import login_user, login_required, logout_user
from wtforms import Form, StringField, PasswordField
from Services.UserService import UserService
from Controllers import session


class LoginForm(Form):
    username = StringField('Username')
    password = PasswordField('Password')

    def validate_on_submit(self):
        return UserService.validate_user(session, self.username.data, self.password.data)


login_page = Blueprint('login', __name__)


@login_page.route('/')
def index():
    return redirect('login')


@login_page.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = UserService.get_user_by_name(session, form.username.data)
        login_user(user)
        flash('Logged in successfully.')

        return redirect(url_for('warning.warning'))
    return render_template('Views/Login/login.html', form=form)


@login_page.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('login')


@login_page.errorhandler(401)
def page_not_found(e):
    return render_template('Views/Login/login.html'), 401
