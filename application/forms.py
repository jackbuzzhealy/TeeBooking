from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Golfers, TimeSlots, Booking, BookingLine
from flask_login import current_user

class RegistrationForm(FlaskForm):
    email = StringField('Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )
    foreName = StringField('First Name',
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
        user = golfers.query.filter_by(email=email.data).first()

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
