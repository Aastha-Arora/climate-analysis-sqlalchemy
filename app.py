import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import datetime as dt
import numpy as np

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to both table
Measurement = Base.classes.measurement
Station = Base.classes.station


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
	return (f'<h4>Welcome to Hawaii climate analysis API</h4>'
			f'Available routes: <br/>'
			f'/api/v1.0/precipitation<br/>'
			f'/api/v1.0/stations<br/>'
			f'/api/v1.0/tobs<br/>'
			f'/api/v1.0/&lt;start_date&gt;<br/>'
			f'/api/v1.0/&lt;start_date&gt;/&lt;end_date&gt;'
			f'<br/><br/>Enter dates in yyyy-mm-dd format')


@app.route("/api/v1.0/precipitation")
def precipitation():
	session = Session (engine)
	
	"""Return precipatition values for last one year data in database"""
	# Calculate the date 1 year ago from last date in database
	year_ago = dt.date(2017,8,23) - dt.timedelta(days = 365)
	# start_date = '2016-08-23'
	results = session.query(Measurement.date, Measurement.prcp)\
		.filter(Measurement.date >= year_ago).all()

	session.close()

	dict_prcp = {result[0]: result[1] for result in results}
	return jsonify(dict_prcp)


@app.route("/api/v1.0/stations")
def station():
	session = Session (engine)

	results = session.query(Station.station).all()

	session.close()
	# Converting results to a list
	station_names = list(np.ravel(results))
	return jsonify(station_names)


@app.route("/api/v1.0/tobs")
def temperature():
	session = Session (engine)
	"""Return temperature observations for last one year data in database"""
	"""Results for most active station"""
	# Calculate the date 1 year ago from last date in database
	year_ago = dt.date(2017,8,23) - dt.timedelta(days = 365)

	results = session.query(Measurement.tobs)\
				.filter(Measurement.station == 'USC00519281')\
				.filter(Measurement.date >= year_ago)\
				.all()

	session.close()
	# Converting results to a list
	list_temp = list(np.ravel(results))
	return jsonify(list_temp)


@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def start(start=None, end=None):
	session = Session (engine)
	"""Return temperature (min, avg and max)"""

	# Select statement
	sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

	if end is None:

		results = session.query(*sel)\
				.filter(Measurement.date >= start).all()
		
		session.close()

		tobs = list(np.ravel(results))
		return jsonify(tobs)

	results = session.query(*sel)\
		.filter(Measurement.date >= start)\
		.filter(Measurement.date <= end).all()

	session.close()

	tobs = list(np.ravel(results))
	return jsonify(tobs)

if __name__ == "__main__":
    app.run(debug=True)
