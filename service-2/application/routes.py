from application import app, db
from application.models import Players
from sqlalchemy import func, select


@app.route('/generate/random/', methods=['GET', 'POST'])
def generate_random():
	player = Players.query.order_by(func.random()).limit(1)
	return render_template('generate/random.html', player=player)
