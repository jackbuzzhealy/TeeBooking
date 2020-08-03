from application import db, login_manager
from flask_login import UserMixin

class Golfer(db.Model, UserMixin):
    email = db.Column(db.String(50), primary_key=True)
    foreName = db.Column(db.String(25), nullable=False, unique=True)
    secondName = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    
    @login_manager.user_loader
    def load_user(id):
   	 return Users.query.get(int(id))

class TimeSlots(db.Model):
    timeID = db.Column(db.Integer, primary_key=True)
    slot = db.Column(db.String(25), nullable=False)

class Booking(db.Model):
     bookingID = db.Column(db.Integer, primary_key=True, autoincrement=True)
     email = db.Column(db.String(50), db.ForeignKey('golfer.email'), nullable=False)

class BookingLine(db.Model):
     lineID = db.Column(db.Integer, primary_key=True, autoincrement=True)
     bookingID = db.Column(db.Integer, db.ForeignKey('booking.bookingID'), nullable=False)
     timeID = db.Column(db.Integer, db.ForeignKey('time_slots.timeID'),nullable=False)
