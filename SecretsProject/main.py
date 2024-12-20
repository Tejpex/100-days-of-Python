from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5


class LogInForm(FlaskForm):
    email = StringField("E-mail:", validators=[DataRequired(), Email(message="Not a valid e-mail.")])
    password = PasswordField("Password: ", validators=[
        DataRequired(),
        Length(min=8, message="Password has to be at least 8 characters.")
    ])
    submit = SubmitField("Log In")


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = ""


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
