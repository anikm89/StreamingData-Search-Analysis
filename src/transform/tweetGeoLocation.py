from time import sleep

import geopy
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim

from src.logs import tweetLogs


def setLocation(location):
    try:
        sleep(2)
        geolocator = Nominatim()
        location = geolocator.geocode(location, exactly_one=True,timeout=5)
        nlocation = (location.latitude, location.longitude)
    except AttributeError as e:
        nlocation =('NA','NA')
        r = "Error: geocode failed on Attribute Error %s with message" % (e.message)
        tweetLogs.geoLogIt(r)
    except GeocoderTimedOut as e:
        nlocation =('NA','NA')
        r ="Error: geocode failed on input %s with message"%(e.message)
        tweetLogs.geoLogIt(r)
    except geopy.exc.GeocoderServiceError as e:
        nlocation =('NA','NA')
        r="Error: geocode service error failed with message %s"%(e.message)
        tweetLogs.geoLogIt(r)
    return nlocation

def getAddress(location):

    try:
        #address=('NA','NA')
        """""
        geolocator = Nominatim()
        location = geolocator.geocode(location, exactly_one=True, timeout=15)
        address = stringFormat(location.address)
        """""
        #print address
    except AttributeError:
        address = 'NA'
    except GeocoderTimedOut as e:
        address = 'NA'
        r = "Error: geocode failed on input %s with message"%(e.message)
        tweetLogs.logIt(r)
    except geopy.exc.GeocoderServiceError as e:
        address = 'NA'
        r="Error: geocode service error failed with message %s"%((e.message))
        tweetLogs.logIt(r)

    return address
