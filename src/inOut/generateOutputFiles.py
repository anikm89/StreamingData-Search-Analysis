import csv
import os
from pandas import DataFrame


currPath = os.getcwd()
PROJECT_DIR=currPath.strip('src')
exportDir = os.path.join(PROJECT_DIR,'OutputFiles')
#f1 = os.path.join(exportDir ,'tweetWordsCounts1.csv')
#f1 = "file://%/OutputFiles/tweetWordsCounts1.csv"%(currPath)
#f2 = "C:\tibco\Anik\workspace\twitterDataAnalysis\StreamTweets\OutputFiles\tweetBigWordsCounts.csv"
def wordCountfile(tweeter):
    with open(os.path.join(exportDir, 'tweetWordsCounts2.csv'), 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in tweeter.items():
           writer.writerow([key, value])

def HashCountFile(tweetHash):
    with open(os.path.join(exportDir,'tweetHashCounts2.csv'), 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in tweetHash.items():
            writer.writerow([key, value])

def BigWordsCountFile (tweetMaxWords):
    with open(os.path.join(exportDir,'tweetBigWordsCounts2.csv'),'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in tweetMaxWords.items():
           writer.writerow([key, value])

def tweetDataCSV(df):
    df.to_csv("tweetDataExport10112016.csv",index=False,sep=';', encoding='utf-8',cols=('CreationTime','Text','Lang','TweetScore','Location','TweetTimeZone','Crime','UserName','ScreenName','url','Candidate','HilaryScore','TrumpScore'))

# """""
