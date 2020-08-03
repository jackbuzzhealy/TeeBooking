from application import db
from flask_login import UserMixin

class tblGolfer(db.Model, UserMixin):
    email = db.Column(db.String(50), primary_key=True)
    foreName = db.Column(db.String(25), nullable=False, unique=True)
    secondName = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

class tblTimeSlots(db.Model):
    timeID = db.Column(db.Integer, primary_key=True)
    slot = db.Column(db.String(25), nullable=False)

class tblBooking(db.Model):
     bookingID = db.Column(db.Integer, primary_key=True, autoincrement=True)
     email = db.Column(db.String(50), db.ForeignKey('tblGolfer.email'), nullable=False)

class tblBookingLine(db.Model):
     lineID = db.Column(db.Integer, primary_key=True, autoincrement=True)
     bookingID = db.Column(db.Integer, db.ForeignKey('tblBooking.bookingID'), nullable=False)
     timeID = db.Column(db.Integer, db.ForeignKey('tblTimeSlots.timeID'),nullable=False)
