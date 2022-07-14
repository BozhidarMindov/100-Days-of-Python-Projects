from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.secret_key = "something-key-related"


class LogInForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    button_submit = SubmitField("Login")


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods = ["GET", "POST"])
def login():
    form_login = LogInForm()
    form_login.validate_on_submit()

    if form_login.validate_on_submit():
        if form_login.email.data == "admin@email.com" and form_login.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html", form=form_login)


if __name__ == '__main__':
    app.run(debug=True)