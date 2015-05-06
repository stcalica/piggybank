from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
	name = StringField('openid', validators=[DataRequired()])
	remember_me = BooleanField('remember_me', default=0)

class SignUpForm(Form):
	name = StringField('name', validators=[DataRequired()])
	email = StringField('email', validators=[DataRequired()])
	