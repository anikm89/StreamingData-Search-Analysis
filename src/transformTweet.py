import tweetLogs
import time
import tweetThreads
import connectDB
import connectDB1
import tweetGeoLocation
import generateOutputFiles
import builTweetDataStruct
import tweetDataAnalyzer
import referenceData
import tweetLogs
from datetime import datetime



scores ={}
counter = 0

def constructString(txt):
    if txt is not None:
        try:
            txt = txt.encode("ascii")
        except UnicodeEncodeError as e:
            txt  = txt.encode("utf-8")
            r = (("UnicodeError: Data Unicode Error %s" % (e.message)) + " " + ("For the follwoing data %s" %(txt)))
            tweetLogs.logIt(r)
    else:
        # value was valid ASCII data
        pass

    return txt

def textWordSplit(txt):
    tweetWords = (''.join(str(e) for e in txt)) # converting to a string
    tweetWords = tweetWords.replace('\n',' ')
    #tweetText2.append(tweetWords)
    tweetWords = tweetWords.split(" ") # splitting inti words
    tweetLen = len(tweetWords)
    return tweetWords

def dateTimeSplit(txt):
    txt = datetime.strptime(txt, '%a %b %d %H:%M:%S +0000 %Y')
    (date, time) = str(txt).split(" ")
    return (date,time)

def stringFormat(txt):
    if txt is not None:
        try:
            txt = txt.replace('\n', '')
            txt = txt.replace('\r', '')
            txt = txt.replace('\r\n', '')
            #txt = txt.replace("'","''")
        except AttributeError as e:
            txt ='NA'
            r = (("UnicodeError: Data Unicode Error %s" % (e.message)) + " " + ("For the follwoing data %s" %(txt)))
            tweetLogs.logIt(r)
            #logging.basicConfig(filename='event.log', level=logging.DEBUG)
            #logging.debug(r)
        return txt

def getTweetText(tweet):
    try:
        txt = stringFormat(constructString(tweet['text']))
    except KeyError as e:
        r = (("KeyError: Data KeyError Error %s" % (e.message)))
        txt = 'NA'
        tweetLogs.logIt(r)
    tweetText = stringFormat(txt)
    return tweetText


def getUserDetails(tweetobj):
    default='NA'
    try:
        tweetuser = tweetobj['user']
    except KeyError as e:
        r = (("KeyError: Data KeyError Error %s" % (e.message)))
        tweetuser = 'NA'
        tweetUserID = 'NA'
        tweetLang = 'NA'
        tweetTimeZone = 'NA'
        tweetCreateAt = 'NA'
        tweetDate = 'NA'
        tweetTime = 'NA'
        tweetLocation = 'NA'
        tweetDescription = 'NA'
        tweetUserName = 'NA'
        tweetUserScreen = 'NA'
        tweetUserUrl = 'NA'
        tweetLatitude = 'NA'
        tweetLongitude = 'NA'
        tweetLogs.logIt(r)

    if tweetuser != 'NA':

        try:
            tweetUserID = tweetuser['id']
        except KeyError as e:
            r = (("KeyError: Data KeyError Error %s" % (e.message)))
            tweetUserID = 'NA'
            tweetLogs.logIt(r)
        try:
            tweetLang = stringFormat(constructString(tweetuser['lang']))
        except KeyError as e:
            r = (("KeyError: Data KeyError Error %s" % (e.message)))
            tweetLang = 'NA'
            tweetLogs.logIt(r)
        try:
            tweetTimeZone = stringFormat(constructString((tweetuser['time_zone'])))
        except KeyError as e:
            r = (("KeyError: Data KeyError Error %s" % (e.message)))
            tweetTimeZone = 'NA'
            tweetLogs.logIt(r)
        try:
            #tweetCreateAt.append(tweetuser['created_at'])
            dateTup = dateTimeSplit(tweetuser.get('created_at', default))
            tweetDate = (dateTup[0])
            tweetTime = (dateTup[1])
        except KeyError as e:
            r = (("KeyError: Data KeyError Error %s" % (e.message)))
            #tweetCreateAt.append('NA')
            tweetDate = 'NA'
            tweetTime = 'NA'
            tweetLogs.logIt(r)
        try:
            tweetLocation = stringFormat(constructString(tweetuser['location']))
        except KeyError as e:
            r = (("KeyError: Data KeyError Error %s" % (e.message)))
            tweetLocation = 'NA'
            tweetLogs.logIt(r)
        try:
            locTuple = tweetGeoLocation.setLocation(stringFormat(constructString(tweetuser['location'])))
            tweetLatitude = locTuple[0]
            tweetLongitude = locTuple[1]
        except KeyError as e:
            r = (("KeyError: Data KeyError Error %s" % (e.message)))
            tweetLatitude = 'NA'
            tweetLongitude = 'NA'
            tweetLogs.logIt(r)
        try:
            tweetUserName = stringFormat(constructString(tweetuser['name']))
        except KeyError as e:
            r = (("KeyError: Data KeyError Error %s" % (e.message)))
            tweetUserName = 'NA'
            tweetLogs.logIt(r)
        try:
            tweetUserScreen = stringFormat(constructString(tweetuser['screen_name']))
        except KeyError as e:
            r = (("KeyError: Data KeyError Error %s" % (e.message)))
            tweetUserScreen = 'NA'
            tweetLogs.logIt(r)
        try:
            tweetUserUrl = stringFormat(constructString(tweetuser['url']))
        except KeyError as e:
            r = (("KeyError: Data KeyError Error %s" % (e.message)))
            tweetUserUrl = 'NA'
            tweetLogs.logIt(r)


        #result = (tweetUserID,tweetLang,tweetTimeZone,tweetCreateAt,tweetLocation,tweetLatitude,tweetLongitude,tweetUserName,tweetUserScreen,tweetUserUrl)
    else:
        tweetUserID = 'NA'
        tweetLang = 'NA'
        tweetTimeZone = 'NA'
        tweetCreateAt = 'NA'
        tweetDate = 'NA'
        tweetTime = 'NA'
        tweetLocation = 'NA'
        tweetDescription = 'NA'
        tweetUserName = 'NA'
        tweetUserScreen = 'NA'
        tweetUserUrl = 'NA'
        tweetLatitude = 'NA'
        tweetLongitude = 'NA'

    result = (tweetUserID, tweetLang, tweetTimeZone, tweetDate, tweetTime, tweetLocation, tweetLatitude, tweetLongitude,
              tweetUserName, tweetUserScreen, tweetUserUrl,tweetuser)
    return result

