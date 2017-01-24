#from __future__ import print_function
import sys
import json
import traceback
from compiler.ast import flatten
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
import nlp

tweetobj = []
tweetRow = []
tweetText = []
tweetForeignText=[]
tweetText1 = []
tweetText2 = []
tweetItemsList =[]
tweetCreateAt = []
tweetLang = []
tweetGeo = []
tweetLocation = []
tweetLatitude =[]
tweetLongitude=[]
tweetTimeZone = []
tweetUser = []
tweetDescription = []
tweetCrime = []
tweetUserName =[]
tweetUserScreen =[]
tweetUserUrl = []
tweetUserID=[]
tweetDate=[]
tweetTime=[]
docID = []

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


def tweetScoreTotal():
    return 0

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, time.ctime(time.time()) )


def getUserDetails(tweet):
    default='NA'
    try:
        tweetuser = tweet['user']
    except KeyError as e:
        r = (("KeyError: Data KeyError Error %s" % (e.message)))
        tweetuser = 'NA'
        tweetLogs.logIt(r)

    if tweetuser != 'NA':

        try:
            tweetUserID.append(tweetuser['id'])
        except KeyError as e:
            r = (("KeyError: Data KeyError Error %s" % (e.message)))
            tweetUserID.append('NA')
            tweetLogs.logIt(r)
        try:
            tweetLang.append(tweetuser['lang'])
        except KeyError as e:
            r = (("KeyError: Data KeyError Error %s" % (e.message)))
            tweetLang.append('NA')
            tweetLogs.logIt(r)

        try:
            tweetTimeZone.append(tweetuser['time_zone'])
        except KeyError as e:
            r = (("KeyError: Data KeyError Error %s" % (e.message)))
            tweetTimeZone.append('NA')
            tweetLogs.logIt(r)
        try:
            tweetDate.append(tweetuser['date'])
            tweetTime.append(tweetuser['time'])
        except KeyError as e:
            r = (("KeyError: Data KeyError Error %s" % (e.message)))
            tweetDate.append('NA')
            tweetTime.append('NA')
            tweetLogs.logIt(r)
        try:
            tweetLocation.append((stringFormat(constructString(tweetuser['location']))))
        except KeyError as e:
            r = (("KeyError: Data KeyError Error %s" % (e.message)))
            tweetLocation.append('NA')
            tweetLogs.logIt(r)
        try:

            tweetLatitude.append(tweetuser['latitude'])
            tweetLongitude.append(tweetuser['longitude'])
        except KeyError as e:
            r = (("KeyError: Data KeyError Error %s" % (e.message)))
            tweetLatitude.append('NA')
            tweetLongitude.append('NA')
            tweetLogs.logIt(r)
        try:
            tweetUserName.append((stringFormat(constructString(tweetuser['name']))))
        except KeyError as e:
            r = (("KeyError: Data KeyError Error %s" % (e.message)))
            tweetUserName.append('NA')
            tweetLogs.logIt(r)
        try:
            tweetUserScreen.append((stringFormat(constructString(tweetuser['screen_name']))))
        except KeyError as e:
            r = (("KeyError: Data KeyError Error %s" % (e.message)))
            tweetUserScreen.append('NA')
            tweetLogs.logIt(r)
        try:
            tweetUserUrl.append((stringFormat(constructString(tweetuser['url']))))
        except KeyError as e:
            r = (("KeyError: Data KeyError Error %s" % (e.message)))
            tweetUserUrl.append('NA')
            tweetLogs.logIt(r)


        #result = (tweetUserID,tweetLang,tweetTimeZone,tweetCreateAt,tweetLocation,tweetLatitude,tweetLongitude,tweetUserName,tweetUserScreen,tweetUserUrl)
        #result = (tweetUserID,tweetLang,tweetTimeZone,tweetDate,tweetTime,tweetLocation,tweetLatitude,tweetLongitude,tweetUserName,tweetUserScreen,tweetUserUrl)
        #return result
    else:
        tweetUserID.append('NA')
        tweetLang.append('NA')
        tweetTimeZone.append('NA')
        tweetCreateAt.append('NA')
        tweetDate.append('NA')
        tweetTime.append('NA')
        tweetLocation.append('NA')
        tweetDescription.append('NA')
        tweetUserName.append('NA')
        tweetUserScreen.append('NA')
        tweetUserUrl.append('NA')
        tweetLatitude.append('NA')
        tweetLongitude.append('NA')

    result = (tweetLang, tweetTimeZone, tweetDate, tweetTime, tweetLocation, tweetLatitude, tweetLongitude,
              tweetUserName, tweetUserScreen, tweetUserUrl)
    return result

def inTweets(tweet,row,query):
    default = 'NA'


    wordsdict = referenceData.AfinDict()
    desc = ''
    txt = ''

    try:
        txt=stringFormat(constructString(tweet['text']))
    except KeyError as e:
        r = (("KeyError: Data KeyError Error %s" % (e.message)))
        txt = 'NA'
        tweetLogs.logIt(r)

    """tweet text Information"""
    tweetText.append(txt)

    """tweet Text Words"""
    tweetWords=textWordSplit(txt)


    """
    Get User information : tweetLang,tweetTimeZone,tweetCreateAt,tweetLocation,tweetLatitude,tweetLongitude,tweetUserName,tweetUserScreen,tweetUserUrl
    """
    (tweetLang, tweetTimeZone, tweetDate, tweetTime, tweetLocation, tweetLatitude, tweetLongitude, tweetUserName, tweetUserScreen, tweetUserUrl) = getUserDetails(tweet)

    """ Sentiment Analysis """
    tweetScore,tweetType = tweetDataAnalyzer.sentimentScore(wordsdict,tweetWords)

    """" crime Analysis """
    tweetCrime = tweetDataAnalyzer.crime(tweetScore[row])

    """ Election Analysis """
    (hscore, dscore, candidate)= tweetDataAnalyzer.presidentialCandidateScoring (tweetWords)

    """ Query Analysis """
    (queryScore, queryList,querySearchResult)= tweetDataAnalyzer.queryResultsScore (tweetWords,query,row,txt)

    """ WordCounts """
    (tweeter, tweetHash, tweetMaxWords)=tweetDataAnalyzer.tweetWordCount(tweetWords)

    """Document ID"""
    docID.append(row)


    #connectDB1.dbConnection1(tweetUserID,tweetText,tweetLang,tweetTimeZone,tweetDate,tweetTime,tweetLocation,tweetLatitude,tweetLongitude,tweetUserName,
    #             tweetUserScreen,tweetUserUrl,tweetScore,tweetCrime,candidate,hscore,dscore,row)

    #row +=1
    #counter = 0

    tweetItemsList =[tweetText,tweetLang,tweetTimeZone,tweetDate,tweetTime,tweetLocation,tweetLatitude,tweetLongitude,tweetUserName,
                     tweetUserScreen,tweetUserUrl,tweetScore,tweetCrime,candidate,hscore,dscore,queryScore, queryList,tweetType,docID]

    #tweetdict = builTweetDataStruct.tweetDictionary(tweetItemsList)
    #df = builTweetDataStruct.buildDataFrame(tweetdict)

    #print tweetdict
    #print df

    generateOutputFiles.wordCountfile(tweeter)
    generateOutputFiles.HashCountFile(tweetHash)
    generateOutputFiles.BigWordsCountFile(tweetMaxWords)
    #generateOutputFiles.tweetDataCSV(df)

    #test =tweetDataAnalyzer.tweetWordCount(tweetWords)

    #print test

    return row,tweetItemsList,querySearchResult

    #Insert Analysis Into Oracle DataBase
    #connectDB.insertIntoDB(tweetdict)

def main():
    sent_file = 'AFINN-111.txt'
    inTweets(sent_file)


if __name__ == '__main__':
    main()
