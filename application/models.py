from application import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return Golfer.query.get(int(id))

class Golfer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    foreName = db.Column(db.String(25), nullable=False)
    secondName = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)

class TimeSlots(db.Model):
    timeID = db.Column(db.Integer, primary_key=True)
    slot = db.Column(db.String(25), nullable=False)

class Booking(db.Model):
     bookingID = db.Column(db.Integer, primary_key=True, autoincrement=True)
     golferID  = db.Column(db.Integer, db.ForeignKey('golfer.id'), nullable=False)

class BookingLine(db.Model):
     lineID = db.Column(db.Integer, primary_key=True, autoincrement=True)
     bookingID = db.Column(db.Integer, db.ForeignKey('booking.bookingID'), nullable=False)
     timeID = db.Column(db.Integer, db.ForeignKey('time_slots.timeID'),nullable=False)
