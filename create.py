from application import db, bcrypt
from application.models import Golfer

db.drop_all()
db.create_all()

golfer1 = Golfer(email="joebloggs@mail.com", foreName="Joe", secondName="Bloggs", password=bcrypt.generate_password_hash("password"))
db.session.add(golfer1)
db.session.commit()
