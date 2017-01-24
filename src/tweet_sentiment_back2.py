#from __future__ import print_function
import sys
import json
import traceback
from compiler.ast import flatten
import time

import connectDB
import connectDB1
import tweetGeoLocation
import generateOutputFiles
import builTweetDataStruct
import tweetDataAnalyzer
import referenceData
import tweetLogs

tweetobj = []
tweetRow = []
tweetText = []
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

scores ={}
counter = 0


def constructString(txt):
    #for j in range(len(txt)):
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
    tweetText2.append(tweetWords)
    tweetWords = tweetWords.split(" ") # splitting inti words
    tweetLen = len(tweetWords)
    return tweetWords

def stringFormat(txt):
    if txt is not None:
        try:
            txt = txt.replace('\n', '')
            txt = txt.replace('\r', '')
            txt = txt.replace('\r\n', '')
            txt = txt.replace("'","''")
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


def getUserDetails(tweetobj):
    default='NA'
    tweetuser = tweetobj.get('user', default)

    if tweetuser != 'NA':
        tweetLang.append(tweetuser.get('lang', default))
        tweetTimeZone.append(tweetuser.get('time_zone', default))
        tweetCreateAt.append(tweetuser.get('created_at', default))
        tweetLocation.append((stringFormat(constructString(tweetuser.get('location', default)))))
        locTuple = tweetGeoLocation.setLocation(stringFormat(constructString(tweetuser.get('location', default))))
        tweetLatitude.append(locTuple[1])
        tweetLongitude.append(locTuple[1])
        # a = tweetLocation
        # tweetDescription.append((tweetuser.get('description',default)))
        tweetUserName.append(stringFormat(constructString(tweetuser.get('name', default))))
        tweetUserScreen.append(stringFormat(constructString(tweetuser.get('screen_name', default))))
        tweetUserUrl.append(stringFormat(constructString(tweetuser.get('url', default))))
    else:
        tweetLang.append('NA')
        tweetTimeZone.append('NA')
        tweetCreateAt.append('NA')
        tweetLocation.append('NA')
        tweetDescription.append('NA')
        tweetUserName.append('NA')
        tweetUserScreen.append('NA')
        tweetUserUrl.append('NA')
        tweetLatitude.append('NA')
        tweetLongitude.append('NA')

    result = (tweetLang,tweetTimeZone,tweetCreateAt,tweetLocation,tweetLatitude,tweetLongitude,tweetUserName,tweetUserScreen,tweetUserUrl)
    return result

def getUserDetails1(tweetobj):
    default='NA'
    tweetuser = tweetobj.get('user', default)

    if tweetuser != 'NA':
        tweetLang.append(tweetuser.get('lang', default))
        tweetTimeZone.append(tweetuser.get('time_zone', default))
        tweetCreateAt.append(tweetuser.get('created_at', default))
        tweetLocation.append((stringFormat(constructString(tweetuser.get('location', default)))))
        locTuple = tweetGeoLocation.setLocation(stringFormat(constructString(tweetuser.get('location', default))))
        tweetLatitude.append(locTuple[1])
        tweetLongitude.append(locTuple[1])
        # a = tweetLocation
        # tweetDescription.append((tweetuser.get('description',default)))
        tweetUserName.append(stringFormat(constructString(tweetuser.get('name', default))))
        tweetUserScreen.append(stringFormat(constructString(tweetuser.get('screen_name', default))))
        tweetUserUrl.append(stringFormat(constructString(tweetuser.get('url', default))))
    else:
        tweetLang.append('NA')
        tweetTimeZone.append('NA')
        tweetCreateAt.append('NA')
        tweetLocation.append('NA')
        tweetDescription.append('NA')
        tweetUserName.append('NA')
        tweetUserScreen.append('NA')
        tweetUserUrl.append('NA')
        tweetLatitude.append('NA')
        tweetLongitude.append('NA')

    result = (tweetLang,tweetTimeZone,tweetCreateAt,tweetLocation,tweetLatitude,tweetLongitude,tweetUserName,tweetUserScreen,tweetUserUrl)
    return result

def inTweets(fp):
    default = 'NA'
    row = 0

    #opentweet = open("output_small.txt","r")
    opentweet = open("twitterPresidentialDebateOut.txt", "r")
    #opentweet = open("output_V1 copy.txt","r")
    #opentweet = open("output_V1.txt","r")
    #opentweet = open("output.txt","r")

    wordsdict = referenceData.AfinDict(fp)
    #crimeWordsList = referenceData.crimeWords()

    for line in opentweet:
        tweetobj = json.loads(line)
        desc = ''
        txt = ''

        txt = tweetobj.get('text', default)                      # Tweet Text Information
        txt = constructString(txt)                               #format the text string
        tweetText.append(stringFormat(txt))


        #tweet Text Words
        tweetWords=textWordSplit(txt)


        # Get User information : tweetLang,tweetTimeZone,tweetCreateAt,tweetLocation,tweetLatitude,tweetLongitude,tweetUserName,
        #tweetUserScreen,tweetUserUrl
        getUserDetails(tweetobj)

        #Sentiment Analysis
        tweetScore = tweetDataAnalyzer.sentimentScore(wordsdict,tweetWords)

        # crime Analysis
        tweetCrime = tweetDataAnalyzer.crime(tweetScore[row])
        #crime(tweetLen,tweetWords,crimeWordsList,tweetScore)

        #Election Analysis
        (hscore, dscore, candidate)= tweetDataAnalyzer.presidentialCandidateScoring (tweetWords)

        #WordCounts
        (tweeter, tweetHash, tweetMaxWords)=tweetDataAnalyzer.tweetWordCount(tweetWords)

        connectDB1.dbConnection1(tweetText,tweetLang,tweetTimeZone,tweetCreateAt,tweetLocation,tweetLatitude,tweetLongitude,tweetUserName,
                     tweetUserScreen,tweetUserUrl,tweetScore,tweetCrime,candidate,hscore,dscore,row)

        row +=1

    #counter = 0

    tweetItemsList =[tweetText,tweetLang,tweetTimeZone,tweetCreateAt,tweetLocation,tweetLatitude,tweetLongitude,tweetUserName,
                     tweetUserScreen,tweetUserUrl,tweetScore,tweetCrime,candidate,hscore,dscore]

    tweetdict = builTweetDataStruct.tweetDictionary(tweetItemsList)
    df = builTweetDataStruct.buildDataFrame(tweetdict)

    generateOutputFiles.wordCountfile(tweeter)
    generateOutputFiles.HashCountFile(tweetHash)
    generateOutputFiles.BigWordsCountFile(tweetMaxWords)
    #generateOutputFiles.tweetDataCSV(df)

    #Insert Analysis Into Oracle DataBase
    #connectDB.insertIntoDB(tweetdict)

def main():
    sent_file = 'AFINN-111.txt'
    inTweets(sent_file)


if __name__ == '__main__':
    main()
