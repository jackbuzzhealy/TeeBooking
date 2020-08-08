from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Golfer, TimeSlots, Booking, BookingLine
from flask_login import current_user
from flask_sqlalchemy import SQLAlchemy
from wtforms_sqlalchemy.fields import QuerySelectField

def slotQuery():
    return TimeSlots.query.all()

def deleteQuery():
    golferID  = current_user.id
    times = []

    bookings = Booking.query.filter_by(golferID=golferID).all()
   
    for booking in bookings:
        lines = BookingLine.query.filter_by(bookingID=booking.bookingID).all()
        for line in lines:
            slots = TimeSlots.query.filter_by(timeID=line.timeID).all()
            for slot in slots:
                times.append(slot)
   
    return times

class bookingForm(FlaskForm):
    options = QuerySelectField(query_factory=slotQuery)        

class deleteForm(FlaskForm):
    options = QuerySelectField(query_factory=deleteQuery)

class RegistrationForm(FlaskForm):
    email = StringField('Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )
    firstName = StringField('First Name',
	validators = [
            DataRequired()
        ]
    )
    secondName = StringField('Second Name',
        validators = [
            DataRequired()
        ]
    )
    password = PasswordField('Password',
        validators = [
            DataRequired(),
        ]
    )
    confirm_password = PasswordField('Confirm Password',
        validators = [
            DataRequired(),
            EqualTo('password')
        ]
    )
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = Golfer.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use')

class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
