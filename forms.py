from flask_wtf import FlaskForms
from wtforms import StringField, SubmitField
from wtforms.validators import  DataRequired

class Booking():
	fullname = StringField(validators=[DataRequired()])
	dob = DateField(validators=[DataRequired()])
	button = SubmitField('Submit')