from application import db
from application.models  import Players
import pandas as pd




db.drop_all()
db.create_all()

data = pd.read_csv('./epldata_final.csv')
data.columns = [0,1,2,3]

for index,rows in data.iterrows():
	player = Players(name = rows[0], club=rows[1], position=rows[2], nationality=rows[3])
	db.session.add(player)
db.session.commit()

