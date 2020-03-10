from application import db

class Players(db.Model):
	id =  db.Column(db.Integer, primary_key=True)
	name = db.Columm(db.String(30), nullable=False, unique=True)
	club = db.Column(db.String(30), nullable=False, unique=False)
	position = db.Column(db.String(10), nullable=False, unique=False)
	nationality = db.Column(db.String(30), nullable=False, unique=False)

