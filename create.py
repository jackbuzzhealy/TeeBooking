from application import db
from application.models import Golfer

db.drop_all()
db.create_all()
