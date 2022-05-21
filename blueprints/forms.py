import wtforms
from wtforms.validators import length, EqualTo


class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=3, max=20)])
    password = wtforms.StringField(validators=[length(min=3, max=20)])
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])


class LogingForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=3, max=20)])
    password = wtforms.StringField(validators=[length(min=3, max=20)])