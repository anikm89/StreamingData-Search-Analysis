from collections import Counter


tweetScore=[]
candidate =[]
queryList =[]
tweetCrime =[]
hscore =[]
dscore =[]
qscore =[]
crimeList = []
tweetType= []
queryDocID =[]
queryDocText = []
queryDocScore =[]
queryDocRank = []

queryDataDict = {}
tweeter = {}
tweetHash={}
tweetMaxWords={}


"""
It calculates the score of tweets
1. Refers to AFINN dictinary words and their associated values
2. Sums up the value of score tweet words found in the reference AFINN file
"""
def sentimentScore(wordsdict,tweetWords):
    counter = 0
    wordFreq = Counter(tweetWords)
    sentWordsList = list(wordsdict.keys())
    sentWordsList = [i.lower() for i in sentWordsList]

    for k, v in wordFreq.iteritems():
        if k.lower() in sentWordsList:
            counter = counter + (wordsdict[k.lower()]*v)

    """"
    for j in range(len(tweetWords)):
        for key1, value1 in wordsdict.iteritems():
            if tweetWords[j].lower() == key1.lower() :
                counter= counter + value1
    """
    tweetScore.append(counter)
    if counter > 0:
        tweetType.append('Positive')
    elif counter < 0:
        tweetType.append('Negative')
    elif counter == 0:
        tweetType.append('Neutral')

    return tweetScore,tweetType



def tweetWordCount1 (tweetWords):
    wordCluster = Counter(tweetWords)
    #print wordCluster.items()
    return wordCluster

"""
It creates a dictionary of words used in tweets and calulating the frequency of the words used in them
"""
def tweetWordCount (tweetWords):
    for j in range(len(tweetWords)):
        if len(tweetWords[j]) > 0:
            if (tweetWords[j]).lower() not in tweeter:
                tweeter[(tweetWords[j]).lower()] = 1
            if (tweetWords[j][0] == '#' and (tweetWords[j]).lower() not in tweetHash):
                tweetHash[(tweetWords[j]).lower()] = 1
            if ((tweetWords[j]).lower() not in tweetMaxWords and len((tweetWords[j]).lower()) > 4 and tweetWords[j][
                0] != '#'):
                tweetMaxWords[(tweetWords[j]).lower()] = 1

            if (tweetWords[j]).lower() in tweeter:
                tweeter[(tweetWords[j]).lower()] += 1
            if (tweetWords[j][0] != '#' and (tweetWords[j]).lower() in tweetHash):
                tweetHash[(tweetWords[j]).lower()] += 1
            if ((tweetWords[j]).lower() in tweetMaxWords and len((tweetWords[j]).lower()) > 4 and tweetWords[j][
                0] != '#'):
                tweetMaxWords[(tweetWords[j]).lower()] += 1
    result = (tweeter,tweetHash,tweetMaxWords)
    return result

"""
It checks if a tweets contains query terms and categorize the tweets accordingly
In this case query words are hardcoded to be 'hilary' or 'Trump'
"""
def presidentialCandidateScoring(tweetWords):
    counter = 0
    hilaryScore = 0
    trumpScore = 0

    hilaryNameList =['hilary',"hilary's",'hillary',"hillary's", 'clinton',"clinton's", '#hilary',"#hilary's",'#hillary',
                                           "#hillary's",'#clinton',"#clinton's", 'hilaryclinton','hillaryclinton', '#hilaryclinton','#hillaryclinton','#voteforhilary',
                                           '#voteforhillary']

    trumpNameList = ['trump',"trump's", 'donald', "donald's", '#trump',"#trump's", '#donald', "#donald's", 'donaldtrump',
                                           "donaldtrump's", '#donaldtrump',"#donaldtrump's",'#votefortrump']
    for j in range(len(tweetWords)):
        try:
            if (tweetWords[j]).lower() in hilaryNameList:
                hilaryScore += 1
            if (tweetWords[j]).lower() in trumpNameList:
                trumpScore += 1
        except AttributeError:
            hilaryScore = 0
            trumpScore = 0

    if (hilaryScore > trumpScore):
        candidate.append('Hilary')
    elif (hilaryScore < trumpScore):
        candidate.append('Trump')
    else:
        candidate.append('Neutral')

    hscore.append(hilaryScore)
    dscore.append(trumpScore)
    result = (hscore,dscore,candidate)
    return result

"""
Based on the twitter score calulcated the tweets are categorized to be either positive or negative
"""
def crime(tweetScore):#tweetLen,tweetWords,crimeWordsList,tweetScore):
    if (tweetScore < 0):
        tweetCrime.append('Negative')
    elif (tweetScore > 0):
        tweetCrime.append('Positive')
    else :
        tweetCrime.append('Neutral')

    return tweetCrime


""" document Ranking """
def docRanking():
    return 1

"""
Determine query results
"""
def queryResultsScore(tweetWords, query,row,text):
    queryScore = 0

    #print query
    for j in range(len(tweetWords)):
        try:
            if (tweetWords[j]).lower() == (query):
                queryScore += 1

        except AttributeError:
            queryScore = 0

    if (queryScore >= 1):
        queryList.append('Yes')
        queryDocID.append(row)
        queryDocText.append(text)
        queryDocScore.append(queryScore)
        querySearchResult = (queryDocID,queryDocText,queryDocScore)

    elif (queryScore < 1) :
        queryList.append('No')
        queryDocID.append(None)
        queryDocText.append(None)
        queryDocScore.append(None)
        querySearchResult = (queryDocID,queryDocText,queryDocScore)
    qscore.append(queryScore)
    result = (qscore,queryList,querySearchResult)
    return result
