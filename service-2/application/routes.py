from application import app, db
from application.models import Players


@app.route('/')
@app.route('/home')
def home():
	return ('hello')

