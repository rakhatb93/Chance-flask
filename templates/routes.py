from app import app
from flask import Flask, render_template

@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/booking')
def book():
	return render_template('booking.html')
