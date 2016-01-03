#!/usr/bin/env python

import os
import xively
import subprocess
import time
import datetime
import requests
from w1thermsensor import W1ThermSensor


# extract feed_id and api_key from environment variables
FEED_ID = os.environ["FEED_ID"]
API_KEY = os.environ["API_KEY"]
DS18 = os.environ["DS18_ID"]
DEBUG = os.environ["DEBUG"] or false

# initialize api client
api = xively.XivelyAPIClient(API_KEY)

# function to read 1 minute load average from system uptime command
def read_ds18_temp():
  if DEBUG:
    print "Reading the DS18B20 sensor"
  sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, DS18_ID)
  return sensor.get_temperature() 

# function to return a datastream object. This either creates a new datastream,
# or returns an existing one
def get_datastream(feed):
  try:
    datastream = feed.datastreams.get("outdoor_temp")
    if DEBUG:
      print "Found existing datastream"
    return datastream
  except:
    if DEBUG:
      print "Creating new datastream"
    datastream = feed.datastreams.create("outdoor_temp", tags="load_01")
    return datastream

# main program entry point - runs continuously updating our datastream with the
# current 1 minute load average
def run():
  print "Starting Xively tutorial script"

  feed = api.feeds.get(FEED_ID)

  datastream = get_datastream(feed)
  datastream.max_value = None
  datastream.min_value = None

  while True:
    outdoor_temp = read_ds18_temp()

    if DEBUG:
      print "Updating Xively feed with value: %s" % outdoor_temp

    datastream.current_value = outdoor_temp
    datastream.at = datetime.datetime.utcnow()
    try:
      datastream.update()
    except requests.HTTPError as e:
      print "HTTPError({0}): {1}".format(e.errno, e.strerror)

    time.sleep(10)

run()
