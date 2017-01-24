from collections import Counter
import pandas as pd
import tweetDataAnalyzer
import getTweetData
import operator



def queryResults (queryTable):

    print '\n'
    print "############  Search Results   #############"
    print " "
    print queryTable
    print " "
    return queryTable

def commonPosts(queryTable):
    qtweets = Counter(queryTable['Text_x']).most_common(5)
    l = range(len(qtweets))

    print "Top Articles or Posts : "
    for i in l:
        print qtweets[i][0]
    #locations ={}
    #locations = Counter(queryTable['Location']).most_common(5)
    locations = Counter(queryTable['Location']).most_common(5)
    print " "
    print "Top Locations : "
    for i in l:
        print locations[i]
    print " "

    result = {}
    n= Counter(queryTable['Location'][queryTable['Crime'].str.contains("Negative")])
    p = Counter(queryTable['Location'][queryTable['Crime'].str.contains("Positive")])
    neu = Counter(queryTable['Location'][queryTable['Crime'].str.contains("Neutral")])

    result = {'Negative':n,'Postive':p, 'Neutral': neu}
    result = pd.DataFrame(result)

    print result

def postSentiment (queryTable):

    print "Post Sentimets :"
    sentiment = Counter(queryTable['Crime'])
    print sentiment

def keyWords(text):
    wlist = []
    count = 0
    for i in text:
        tweetWords = getTweetData.textWordSplit(text)
        wlist.append(tweetWords)
        (tweeter, tweetHash, tweetMaxWords) = tweetDataAnalyzer.tweetWordCount(tweetWords)
        #print tweeter
        #print tweetHash
    print "Keywords"
    tweetMaxWords_x = sorted(tweetMaxWords.items(), key=operator.itemgetter(1),reverse=True)
    #print tweetMaxWords_x
    for k,v in tweetMaxWords_x:
        print k, v
        count = count +1
        if count > 10:
            break
def dummyApply(text):
    if len(text) > 0:
        return 'YES'
    else:
        return 'NO'







