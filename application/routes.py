from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from application.forms import RegistrationForm, LoginForm, bookingForm, deleteForm
from application import app, db, bcrypt
from application.models import Golfer, TimeSlots, Booking, BookingLine
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField
from flask_login import current_user
import sys
import datetime
#-------------------------------------------------------
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')
#--------------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = Golfer.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else:
				return redirect('home')
	return render_template('login.html', title='Login', form=form)
#-------------------------------------------------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hash_pw = bcrypt.generate_password_hash(form.password.data)
		user = Golfer(
			foreName=form.firstName.data,
			secondName=form.secondName.data,
			email=form.email.data,
			password=hash_pw
			)

		db.session.add(user)
		db.session.commit()

		return redirect(url_for('home'))

	return render_template('register.html', title='Register', form=form)
#-------------------------------------------------------------
@app.route('/timesheet', methods=['GET','POST'])
def timesheet():
    times = TimeSlots.query.all()
    return render_template('timesheet.html', title='Timesheet', times=times)
#-------------------------------------------------------------
@app.route('/createBooking', methods=['GET','POST'])
@login_required
def createBooking():
    form = bookingForm()
    if form.validate_on_submit():
       golfer = Golfer.query.filter_by(email=current_user.email).first()
       golferID = golfer.id
       slot = TimeSlots.query.filter_by(slot=str(form.options.data)).first()
       slotID = slot.timeID
       dateTime = datetime.datetime.now()

       booking = Booking(golferID=golferID, date=dateTime)
       db.session.add(booking)
       db.session.commit()

       bookingID = booking.bookingID
       line = BookingLine(bookingID=bookingID, timeID=slotID)
       db.session.add(line)
       db.session.commit()

    return render_template('createBooking.html', title='Create Booking', form=form)
#-------------------------------------------------------------
@app.route('/deleteBooking', methods=['GET','POST'])
@login_required
def deleteBooking():
    form = deleteForm()
    if form.validate_on_submit():
        slot = TimeSlots.query.filter_by(slot=str(form.options.data)).first()
        line =  BookingLine.query.filter_by(timeID=slot.timeID).first()
        booking = Booking.query.filter_by(bookingID=line.bookingID).first()
        db.session.delete(line)
        db.session.commit()
        db.session.delete(booking)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('deleteBooking.html', title='Delete Booking', form=form)
#-------------------------------------------------------------
@app.route('/updateBooking', methods=['GET','POST'])
@login_required
def updateBooking():
    oldTimeForm  = deleteForm()
    newTimeForm = bookingForm()
    oldTime = str(oldTimeForm.options.data)
    newTime = ""
    
    if newTimeForm.validate_on_submit() and  oldTime != "":
       newTime = str(newTimeForm.options.data)
       golfer = Golfer.query.filter_by(email=current_user.email).first()
       golferID = golfer.id
       qryBookings = Booking.query.filter_by(golferID=golferID).all()
       
       bookingIDs = []
       times = []
       for i in qryBookings:
           id = i.bookingID
           bookingIDs.append(id)
           for i in bookingIDs:
               qryLines = BookingLine.query.filter_by(bookingID=i).all()
               for i in qryLines:
                   time = i.timeID
                   times.append(time)
        
       qryNewTimeID = TimeSlots.query.filter_by(slot=newTime).first()
       qryUpdating = BookingLine.query.filter_by(timeID=oldTime).first()
       qryUpdating.timeID = qryNewTimeID.timeID
       db.session.commit()

    return render_template('updateBooking.html', title='Update Booking', oldTimeForm=oldTimeForm, newTimeForm=newTimeForm)
#-------------------------------------------------------------
@app.route('/account')
@login_required
def account():
    golfer = Golfer.query.filter_by(email=current_user.email).first()
    
    golferID = golfer.id
    golferForeName = golfer.foreName
    golferSecondName = golfer.secondName

    qryBookings = Booking.query.filter_by(golferID=golferID).all()
    timeIDs  = []
    for i in qryBookings:
        bookingIDs = i.bookingID
        qryBookingID = BookingLine.query.filter_by(bookingID=bookingIDs).all()
        for i in qryBookingID:
            id = i.timeID
            timeIDs.append(id)

    times = []
    for i in timeIDs:
        timeIDs = i
        qryTimes = TimeSlots.query.filter_by(timeID=timeIDs).all()
        for i in qryTimes:
            slot = i.slot
            times.append(slot)
            

    return render_template('account.html', title='Account', ID=str(golferID), foreName=golferForeName, secondName=golferSecondName, times=times)
#--------------------------------------------------------------
@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))
