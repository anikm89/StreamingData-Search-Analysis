import logging
from datetime import datetime
import os

currPath = os.getcwd()
PROJECT_DIR=currPath.strip('src')
exportDir = os.path.join(PROJECT_DIR,'logs')
eventlog = os.path.join(exportDir,'event.log')
geoEventlog = os.path.join(exportDir,'geoEvent.log')
dbEventlog = os.path.join(exportDir,'dbevent.log')

def logIt(r):
    r = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  + ":" + r
    logging.basicConfig(filename= eventlog, level=logging.DEBUG)
    logging.debug(r)

def geoLogIt(r):
    r = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + r
    logging.basicConfig(filename= geoEventlog, level=logging.DEBUG)
    logging.debug(r)

def dbLogIt(r):
    r = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  + ":" + r
    logging.basicConfig(filename= dbEventlog, level=logging.DEBUG)
    logging.debug(r)