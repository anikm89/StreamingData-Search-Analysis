import json
import urllib2 as urllib

import oauth2 as oauth
from pymongo import MongoClient

from src.transform import transformTweet as ts

# See assignment1.html instructions or README for how to get these credentials

api_key = "5dFMHo5U8LbisnJxGCeSaa7IE"
api_secret = "r9lA5kONuP4V1qIw4zTkTw8okIDGlqbfqOoZTLVBuGOpJrpwrN"
access_token_key = "2400851864-PBTjED7StP0A7Q4eM3n8dS4YElYfWSgFw3yrONv"
access_token_secret = "l4YzX795lAf2FDMeu7hfMllNHyDiTCd0s8CYZRQPM0RKU"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''

def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url,
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def connectMongo(post):
    #print post
    client = MongoClient('localhost', 27017)
    db = client['twitter_db']
    collection = db['twitter_collection_cricket_011917']
    #tweet = json.loads(post)
    collection.insert(post)


def fetchsamples():
  #url = "https://stream.twitter.com/1.1/statuses/filter.json?track=president,PRESIDENT,President,pres,obama,hilary,donald,trump,clinton, debate, presidential, DEBATE, Debate,food, entertainment,stocks,movies,crime,trending, politics, intelligence, artificial"
  #url = "https://stream.twitter.com/1.1/statuses/filter.json?track=television,tv, stocks,tesla,uber,crime,apple,food,entertainment,stocks,movies,crime,trending,AI,intelligence,artificial"
  url = "https://stream.twitter.com/1.1/statuses/filter.json?track=cricket,yuvi,yuvraj,dhoni,mahi,india vs enngland,india,indveng"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  for post in response:
      tweetobj = json.loads(post)

      #print post
      default = 'NA'
      #tweetuser = tweetobj.get('user', default)


      """transforming streaming twitter data"""
      """get tweet user deatils"""
      tweetText = ts.getTweetText(tweetobj)
      userDeatils = ts.getUserDetails(tweetobj)
      tweetUserID = userDeatils[0]
      tweetLang = userDeatils[1]
      tweetTimeZone = userDeatils[2]
      tweetDate = userDeatils[3]
      tweetTime = userDeatils[4]
      tweetLocation = userDeatils[5]
      tweetLatitude = userDeatils[6]
      tweetLongitude = userDeatils[7]
      tweetUserName = userDeatils[8]
      tweetUserScreen = userDeatils[9]
      tweetUserUrl = userDeatils[10]
      tweetuser =  userDeatils[10]

      """updating streaming tweet object beforing storing in mangoDB"""
      tweetobj['text'] = tweetText

      if tweetuser != 'NA':
          tweetobj['user']['lang'] = tweetLang
          tweetobj['user']['time_zone'] = tweetTimeZone
          tweetobj['user']['date'] = tweetDate
          tweetobj['user']['time'] = tweetTime
          tweetobj['user']['name'] = tweetUserName
          tweetobj['user']['screen_name'] = tweetUserScreen
          tweetobj['user']['url'] = tweetUserUrl
          tweetobj['user']['location'] = tweetLocation
          tweetobj['user']['latitude'] = tweetLatitude
          tweetobj['user']['longitude'] = tweetLongitude
          tweetobj['user']['tID'] = tweetUserID
      else:
          print 'cannot transform'
      #print tweetobj
      connectMongo(tweetobj)

      print tweetobj

      #line.write("twitterOutSamples.json")

if __name__ == '__main__':
  fetchsamples()

