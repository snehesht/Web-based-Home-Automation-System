#!/usr/bin/python
# Home Automation with RaspberryPI, Arduino and Xbee
# Author : Snehesh Thalapaneni
# Email : snehesh.thalapaneni@hotmail.com

import MySQLdb as mdb
import sys
import serial

def send_data(change):
        ser = serial.Serial('/dev/ttyUSB0', 9600)
        ser.write('%s\n' % change)
        print 'Sending "%s"' % change
        
def fetchstatus():
        try:
          con = mdb.connect('localhost', 'root', 'raspberrypi', 'pro')
          cur = con.cursor()
          # Make a Read SQL query
          query = "SELECT item,status FROM status"
          # Execute sql query
          cur.execute(query)
          fetched_data = cur.fetchall()
          # print fetched_data
        except mdb.Error, e:
          print "Error %d: %s" % (e.args[0],e.args[1])
          sys.exit(1)
        finally:
          if con:
                con.close()
        return fetched_data
# Previous values to check
prv_alarmstatus=1;
prv_acstatus=1;
prv_lightstatus=1;

# Infinite Loop to fetch data from mysql db and check whether if there are any changes
while(1):
  data=fetchstatus()
  #  print data
  # Data Sorting
  alarm=data[0]
  light=data[1]
  ac=data[2]
  alarmstatus=alarm[1]
  lightstatus=light[1]
  acstatus=ac[1]
  # Checking for any changes
  if (prv_lightstatus!=lightstatus or prv_acstatus!=acstatus or prv_alarmstatus!=alarmstatus):
        if (prv_lightstatus!=lightstatus):
              print "light"
              send_data("L")
        if (prv_acstatus!=acstatus):
              print "AC"
              send_data("F")
        if (prv_alarmstatus!=alarmstatus):
              print "Alarm"
              send_data("A")
  prv_alarmstatus=alarmstatus
  prv_acstatus=acstatus
  prv_lightstatus=lightstatus
