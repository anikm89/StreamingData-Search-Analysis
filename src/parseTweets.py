import time
from collections import Counter
import pandas as pd
from pymongo import MongoClient
from src.analyze import searchQueryResults
from src.transform import builTweetDataStruct, getTweetData

tweetItemsList =[]
query ="obama"

print "query sent for search: ", query
print " "
def connectMongo():
    client = MongoClient('localhost', 27017)
    db = client['twitter_db']
    collection = db['twitter_collection_120416_4']
    tweets_iterator = collection.find(no_cursor_timeout=True)
    row = 0

    for tweet in tweets_iterator:
        #(row,tl)=tweet_sentiment.inTweets(tweet,row,query)
        (row,tl,querySearchResult)= getTweetData.inTweets(tweet, row, query)
        row = row + 1
        #print row

    """Overall Results"""
    tweetdict = builTweetDataStruct.tweetDictionary(tl)
    df = builTweetDataStruct.buildDataFrame(tweetdict)
    #print df[0:20]
    commonTweets = Counter(df['Text'].dropna()).most_common(10)
    #print commonTweets
    sentimentType = Counter(df['TweetType'])
    #print sentimentType



    """Query Results"""
    qdf = builTweetDataStruct.tranformQueryResults(querySearchResult)
    queryTable = pd.merge(qdf, df, on='ID')
    searchQueryResults.queryResults(queryTable)
    searchQueryResults.commonPosts(queryTable)
    searchQueryResults.postSentiment(queryTable)
    searchQueryResults.keyWords(queryTable['Text_x'])

    #queryTable['Text_x'] = queryTable.apply(searchQueryResults.dummyApply)
    print queryTable




    #newPlotting.piePlot(sentimentType['Neutral'], sentimentType['Positive'], sentimentType['Negative'])
    #newPlotting.dataTable(commonTweets)
    start_time = time.clock()
    print time.clock() - start_time, "seconds"



def main():
    sent_file = 'AFINN-111.txt'
    print 'Please Wait for Results to load ..............'
    connectMongo()

if __name__ == '__main__':
    main()


