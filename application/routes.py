from flask import render_template
from application import app, db
from application.models import Golfer, TimeSlots, Booking, BookingLine

@app.route('/')
@app.route('/home')
def home():
    Golfers = Golfer.query.all()
    return render_template('home.html', title='Home', Golfers=Golfers)
#--------------------------------------------------------
@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html', title='Login')
#-------------------------------------------------------------
@app.route('/')
@app.route('/register')
def register():
    return render_template('register.html', title='Register')
#-------------------------------------------------------------
@app.route('/')
@app.route('/timesheet')
def timesheet():
    return render_template('timesheet.html', title='Timesheet')
#-------------------------------------------------------------
@app.route('/')
@app.route('/account')
def account():
    return render_template('account.html', title='Account')
#-------------------------------------------------------------
@app.route('/')
@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))
