import numpy as np
import pandas as pandas
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
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
def home_page():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    
    """Using the query from part 1, the most recent 12 months of precipitation data, convert the query results to a dictionary using date as the key and prcp as the value. Return the JSON representation of your dictionary (note the specific format of your dictionary as required from above)."""
    
    session = Session(engine)

    """Return a list of all precipiation values for the last 12 months"""
    # Example # results = session.query(Passenger.name).all()


    results = session.query(Measurement.date, func.avg(Measurement.prcp)).\
    filter(Measurement.date > '2016-08-23').\
    group_by(Measurement.date).\
    order_by(Measurement.date).all()

   # Close session

    session.close()

    prcp = []
    
    for date, average  in results:
        prcp_dict = {}
        prcp_dict['Date'] = date
        prcp_dict['Avg. Precipitation'] = average
        prcp.append(prcp_dict)
    
    # jsonify the results
    return jsonify(prcp)

    # Convert list of tuples into normal list
    # Example # all_names = list(np.ravel(results))


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    
    # """Return a JSON list of stations from the dataset.""""

    
    session = Session(engine)


    # Example: results = session.query(Passenger.name).all()


    results = session.query(Station.station, func.count(Measurement.station)).filter(Station.station == Measurement.station).\
    group_by(Station.station).\
    order_by(func.count(Measurement.station).desc()).all()

   # Close session
    session.close()

    station_list = list(np.ravel(results))

    return jsonify(station_list)

    # OR #station = [] 

    # for name in results:
        #station_dict = {}
        #station_dict['Name'] = name
        #station.append(station_dict)
    
      #jsonify the results
    #return jsonify(station)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Query the dates and temperature observations of the most active station for the latest year of data."""
    """Return a JSON list of temperature observations (TOBS) for that year."""
   
   # Query all passengers
   # results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()

    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > '2016-08-23',Measurement.station == 'USC00519281').\
    group_by(Measurement.date).\
    order_by(Measurement.date).all()
    
    #Close session 

    session.close()

    # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    # jsonify the results

    tobs = []
    for date, temp in results:
        station_tobs={}
        station_tobs['Date'] = date
        station_tobs['Tobs'] = temp
        tobs.append(station_tobs)

    # jsonify the results
    return jsonify(tobs)


@app.route("/api/v1.0/<start>")
def start (start):
    """ Create a query that returns the minimum temperature, the average temperature, and the max temperature for a given start or start-end range."""
    """ When given the start date only, calculate min, max, and avg for all dates greater than and equal to the start date."""

    start = start

    session = Session(engine)
    
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start).all()

    session.close()

    temp_start_list = list(np.ravel(results))

    return jsonify(temp_start_list)


@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    """Create a query that returns the minimum temperature, the average temperature, and the max temperature for a given start or start-end range."""
    """When given the start and the end date, calculate the min, avg, and max for dates between the start and end date inclusive."""
    """Return a JSONified dictionary of min, max, and avg temperatures."""

    start = start 
    end = end 

    session = Session(engine)

    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()

#Close session
    session.close()

    temp_start_end_list = list(np.ravel(results))

    return jsonify(temp_start_end_list)

if __name__ == '__main__':
    app.run(debug=True)
