from flask import Flask, render_template, redirect, url_for, request
from app import app
from app import Book
from forms import *

@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/booking', methods = ['GET', 'POST'])
def booking():
	form=forms.Booking()
	if form.validate_on_submit():
		u = app.Book(fullname=form.fullname.data, dob=form.dob.data)
		db.session.add(u)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('booking.html')

@app.route('/cost', methods = ['GET', 'POST'])
def cost():
	if request.method == 'GET':
		return render_template('cost.html')
	return render_template('index.html')	