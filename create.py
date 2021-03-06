from application import db, bcrypt
from application.models import Golfer, TimeSlots

db.drop_all()
db.create_all()

golfer1 = Golfer(email="healy@mail.com", foreName="Jack", secondName="Healy", password=bcrypt.generate_password_hash("password"))
db.session.add(golfer1)

time1 = TimeSlots(slot="07:00")
db.session.add(time1)
time2 = TimeSlots(slot="07:15")
db.session.add(time2)
time3 = TimeSlots(slot="07:30")
db.session.add(time3)
time4 = TimeSlots(slot="07:45")
db.session.add(time4)
time5 = TimeSlots(slot="08:00")
db.session.add(time5)
time6 = TimeSlots(slot="08:15")
db.session.add(time6)
time7 = TimeSlots(slot="08:30")
db.session.add(time7)
time8 = TimeSlots(slot="08:45")
db.session.add(time8)
time9 = TimeSlots(slot="09:00")
db.session.add(time9)
time10 = TimeSlots(slot="09:15")
db.session.add(time10)
time11 = TimeSlots(slot="09:30")
db.session.add(time11)
time12 = TimeSlots(slot="09:45")
db.session.add(time12)
time13 = TimeSlots(slot="10:00")
db.session.add(time13)
time14 = TimeSlots(slot="10:15")
db.session.add(time14)
time15 = TimeSlots(slot="10:30")
db.session.add(time15)
time16 = TimeSlots(slot="10:45")
db.session.add(time16)
time17 = TimeSlots(slot="11:00")
db.session.add(time17)
time18 = TimeSlots(slot="11:15")
db.session.add(time18)
time19 = TimeSlots(slot="11:30")
db.session.add(time19)
time20 = TimeSlots(slot="11:45")
db.session.add(time20)
time21 = TimeSlots(slot="12:00")
db.session.add(time21)
time22 = TimeSlots(slot="12:15")
db.session.add(time22)
time23 = TimeSlots(slot="13:30")
db.session.add(time23)
time24 = TimeSlots(slot="13:45")
db.session.add(time24)
time25 = TimeSlots(slot="14:00")
db.session.add(time25)
time26 = TimeSlots(slot="14:15")
db.session.add(time26)
time27 = TimeSlots(slot="14:30")
db.session.add(time27)
time28 = TimeSlots(slot="15:45")
db.session.add(time28)
time29 = TimeSlots(slot="16:00")
db.session.add(time29)
time30 = TimeSlots(slot="16:15")
db.session.add(time30)
time31 = TimeSlots(slot="16:30")
db.session.add(time31)
time32 = TimeSlots(slot="16:45")
db.session.add(time32)
time33 = TimeSlots(slot="17:00")
db.session.add(time33)
time34 = TimeSlots(slot="17:15")
db.session.add(time34)
time35 = TimeSlots(slot="17:30")
db.session.add(time35)
time36 = TimeSlots(slot="17:45")
db.session.add(time36)
time37 = TimeSlots(slot="18:00")
db.session.add(time37)
time38 = TimeSlots(slot="18:15")
db.session.add(time38)
time39 = TimeSlots(slot="18:30")
db.session.add(time39)
time40 = TimeSlots(slot="18:45")
db.session.add(time40)
time41 = TimeSlots(slot="19:00")
db.session.add(time41)
time42 = TimeSlots(slot="19:15")
db.session.add(time42)
time43 = TimeSlots(slot="19:30")
db.session.add(time43)

db.session.commit()
