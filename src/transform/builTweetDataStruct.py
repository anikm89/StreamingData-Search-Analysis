from pandas import DataFrame
import pandas as pd
from operator import is_not
from functools import partial

tweetdict={}

queryResultDict = {}

def tweetDictionary(tweetItemsList):
    tweetText = tweetItemsList[0]
    tweetLang = tweetItemsList[1]
    tweetTimeZone = tweetItemsList[2]
    tweetDate = tweetItemsList[3]
    tweetTime = tweetItemsList[4]
    #tweetCreateAt = tweetItemsList[3]
    tweetLocation = tweetItemsList[5]
    tweetLatitude = tweetItemsList[6]
    tweetLongitude = tweetItemsList[7]
    tweetUserName = tweetItemsList[8]
    tweetUserScreen = tweetItemsList[9]
    tweetUserUrl = tweetItemsList[10]
    tweetScore = tweetItemsList[11]
    tweetCrime = tweetItemsList[12]
    candidate = tweetItemsList[13]
    hscore = tweetItemsList[14]
    dscore = tweetItemsList[15]
    queryScore = tweetItemsList[16]
    queryList = tweetItemsList[17]
    tweetType = tweetItemsList[18]
    docID = tweetItemsList[19]




    # constructing a dictionary
    tweetdict['Text'] = tweetText
    tweetdict['Lang'] = tweetLang
    #tweetdict['Description'] = tweetDescription
    tweetdict['TimeZone'] = tweetTimeZone
    #tweetdict['CreationTime'] = tweetCreateAt
    tweetdict['Date'] = tweetDate
    tweetdict['Time'] = tweetTime
    tweetdict['Location'] = tweetLocation
    tweetdict['Latitude'] = tweetLatitude
    tweetdict['Longitude'] = tweetLongitude
    tweetdict['tweetUserName'] = tweetUserName
    tweetdict['tweetUserScreen'] = tweetUserScreen
    tweetdict['tweetUserUrl'] = tweetUserUrl
    tweetdict['tweetScore'] = tweetScore
    tweetdict['Crime'] = tweetCrime
    tweetdict['Candidate'] = candidate
    tweetdict['HilaryScore'] = hscore
    tweetdict['TrumpScore'] = dscore
    tweetdict['QueryScore'] = queryScore
    tweetdict['QueryList'] = queryList
    tweetdict['TweetType'] = tweetType
    tweetdict['ID'] = docID

    #buildDataFrame (tweetdict)

    return tweetdict

def buildDataFrame(tweetdict):
    df = DataFrame({'Date':tweetdict['Date'],
                    'Time':tweetdict['Time'],
                    'Text':tweetdict['Text'],
                    'Lang': tweetdict['Lang'],
                    'TweetScore': tweetdict['tweetScore'],
                    'Location': tweetdict['Location'],
                    'TweetTimeZone': tweetdict['TimeZone'],
                    'Crime': tweetdict['Crime'],
                    'UserName':tweetdict['tweetUserName'],
                    'tweetUserScreen':tweetdict['tweetUserScreen'],
                    'url':tweetdict['tweetUserUrl'],
                    'Candidate': tweetdict['Candidate'],
                    'HilaryScore': tweetdict['HilaryScore'],
                    'TrumpScore': tweetdict['TrumpScore'],
                    'QueryScore':tweetdict['QueryScore'],
                    'QueryList': tweetdict['QueryList'],
                    'TweetType': tweetdict['TweetType'],
                    'ID': tweetdict['ID']})

    return df

def tranformQueryResults(querySearchResult):
    pd.set_option('display.expand_frame_repr', False)
    queryResultDict['ID'] = [i for i in querySearchResult[0] if i is not None]
    queryResultDict['Text'] = [i for i in querySearchResult[1] if i is not None]
    queryResultDict['Score'] = [i for i in querySearchResult[2] if i is not None]

    queryDataTable = DataFrame({'ID':queryResultDict['ID'],
                    'Text':queryResultDict['Text'],
                    'Score': queryResultDict['Score']})
    #queryResulthTable = DataFrame(queryResultDict, index=[0])
    return queryDataTable
