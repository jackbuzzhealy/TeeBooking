from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField
from application import db, bcrypt, app
from application.models import Golfer, TimeSlots, Booking, BookingLine

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


