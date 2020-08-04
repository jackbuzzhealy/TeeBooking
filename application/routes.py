from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from application.forms import RegistrationForm, LoginForm
from application import app, db
from application.models import Golfer, TimeSlots, Booking, BookingLine

@app.route('/')
@app.route('/home')
def home():
    Golfers = Golfer.query.all()
    return render_template('home.html', title='Home', Golfers=Golfers)
#--------------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = Users.query.filter_by(email=form.email.data).first()
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
		user = Users(
			firstName=form.firstName.data,
			secondName=form.secondName.data,
			email=form.email.data,
			password=hash_pw
			)

		db.session.add(user)
		db.session.commit()

		return redirect(url_for('account'))

	return render_template('register.html', title='Register', form=form)
#-------------------------------------------------------------
@app.route('/timesheet')
@login_required
def timesheet():
    times = TimeSlots.query.all()
    return render_template('timesheet.html', title='Timesheet', times=times)
#-------------------------------------------------------------
@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')
#-------------------------------------------------------------
@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))
