"""
Very simple Flask web site, with one page
displaying a course schedule.

"""

import flask
from flask import render_template
from flask import request
from flask import url_for
from flask import jsonify # For AJAX transactions

import json
import logging
import calculate

# Date handling
import arrow # Replacement for datetime, based on moment.js
import datetime # But we still need time
from dateutil import tz  # For interpreting local times

# Our own module
# import acp_limits


###
# Globals
###
app = flask.Flask(__name__)
import CONFIG

import uuid
app.secret_key = str(uuid.uuid4())
app.debug=CONFIG.DEBUG
app.logger.setLevel(logging.DEBUG)


###
# Pages
###

@app.route("/")
@app.route("/index")
@app.route("/calc")
def index():
  app.logger.debug("Main page entry")
  return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] =  flask.url_for("index")
    return flask.render_template('page_not_found.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############


@app.route("/_set_brevet")
def set_brevet():
  """
  sets the brevet distance
  """
  app.logger.debug("Got a JSON request");
  calculate.brevet = request.args.get('brevet', 0, type=int)
  return jsonify(result=calculate.brevet)


@app.route("/_set_sdate")
def set_sdate():
  '''
  sets the starting date
  '''
  app.logger.debug("Got a JSON request")
  sdate = request.args.get('sdate')
  date = sdate.split("-")
  calculate.startdatetime = calculate.startdatetime.replace(year=int(date[0]), month=int(date[1]), day=int(date[2]))
  print('updated start date = {}'.format(calculate.startdatetime))
  return jsonify(result=calculate.startdatetime.isoformat())

@app.route("/_set_stime")
def set_stime():
  '''
  sets the starting time
  '''
  app.logger.debug("Got a JSON request");
  stime = request.args.get('stime')
  time = stime.split(':')
  calculate.startdatetime = calculate.startdatetime.replace(hour=int(time[0]), minute=int(time[1]))
  print('updated start time = {}'.format(calculate.startdatetime))
  return jsonify(result=calculate.startdatetime.isoformat())

@app.route("/_set_units")
def set_units():
  """
  sets the units needed to calculate brevet times
  """
  app.logger.debug("Got a JSON request");
  calculate.units = request.args.get('unit')
  print("units = {}".format(calculate.units))
  return jsonify(result=calculate.units)


@app.route("/_calc_times")
def calc_times():
  """
  Calculates open/close times from miles, using rules
  described at http://www.rusa.org/octime_alg.html.
  Expects one URL-encoded argument, the number of miles.
  """
  app.logger.debug("Got a JSON request");

  dist = request.args.get('dist', 0, type=int)

  tmp = calculate.calc(dist)
  if (tmp == -1):
      return jsonify(result="Distance is more than 10% of the brevet distance.")
  start = tmp[0].format("MM/DD/YYYY HH:mm")
  end = tmp[1].format("MM/DD/YYYY HH:mm")
  returnvalue = "open: {} | close: {}".format(start, end)
  return jsonify(result=returnvalue)

#################
#
# Functions used within the templates
#
#################

@app.template_filter( 'fmtdate' )
def format_arrow_date( date ):
    try:
        normal = arrow.get( date )
        return normal.format("ddd MM/DD/YYYY")
    except:
        return "(bad date)"

@app.template_filter( 'fmttime' )
def format_arrow_time( time ):
    try:
        normal = arrow.get( date )
        return normal.format("hh:mm")
    except:
        return "(bad time)"



#############


if __name__ == "__main__":
    import uuid
    app.secret_key = str(uuid.uuid4())
    app.debug=CONFIG.DEBUG
    app.logger.setLevel(logging.DEBUG)
    app.run(port=CONFIG.PORT, host="0.0.0.0")
