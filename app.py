from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from routes import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Book(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	fullname = db.Column(db.String(200), nullable=False)
	dob = db.Column(db.Date, nullable=False)
	booking_date = db.Column(db.DateTime, default=datetime.utcnow())

	def __repr__(self):
		return '<User %r>' % self.id

if __name__ == '__main__':
    app.run(debug=True)