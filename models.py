from app import app
from app import db

class Book(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	fullname = db.Column(db.String(200), nullable=False)
	dob = db.Column(db.Date, nullable=False)
	booking_date = db.Column(db.Datetime, default=datetime.utcnow)
		