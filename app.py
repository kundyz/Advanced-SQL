import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from flask import Flask

engine = create_engine("sqlite:///Resources/hawaii.sqlite?check_same_thread=False")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

app = Flask(__name__)

@app.route("/")
def home_route():
    return(
        f"Available Routes: <br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    prcp = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > '2017-01-01').all()
    prcp_dict = dict(prcp)
    print("Precipitation")
    return jsonify(prcp_dict)

@app.route("/api/v1.0/stations")
def stations():
    stations = session.query(Station.station).all()
    stations_list = list(np.ravel(stations))
    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    temp = session.query(Measurement.tobs).order_by(Measurement.date).all()
    print("Temperature")
    return jsonify(temp)

@app.route("/api/v1.0/<start>")
def start_date(start):
    start_date = session.query(Station.id, Station.station, func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start).group_by(Station.station).order_by(Station.id).all()
    print("Start date ({start})")
    return jsonify(start_date)

@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    start_end_date = session.query(Station.id, Station.station, func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).group_by(Station.station).order_by(Station.id).all()
    print("Start date ({start}) and end date ({end})")
    return jsonify(start_end_date)

if __name__ == '__main__':
    app.run(debug=False)