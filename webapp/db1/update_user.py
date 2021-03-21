from db import db_session
from models import User

user = User.query.first()
user.salary += 200
db_session.commit()