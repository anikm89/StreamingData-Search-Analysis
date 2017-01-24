import cx_Oracle
import logging
import tweetLogs

k = []
l = []

def insertIntoDB1(tweetdict):
    for key, value in tweetdict.items():
        k.append(key)
        l.append(value)
        #print l
    dbConnection1(k, l)

def dbConnection1(tweetUserID,tweetText,tweetLang,tweetTimeZone,tweetDate,tweetTime,tweetLocation,tweetLatitude,tweetLongitude,tweetUserName,
                     tweetUserScreen,tweetUserUrl,tweetScore,tweetCrime,candidate,hscore,dscore,row):
    con = cx_Oracle.connect('system/admin@localhost/xe')
    cur = con.cursor()
    table_name = "TWITTER_DATA_TABLE"
    keyList =['ID','Text','Lang','TimeZone','TDATE','TTIME','Location','Latitude','Longitude','tweetUserName',
                     'tweetUserScreen','tweetUserUrl','tweetScore','Category','Candidate','HilaryScore','TrumpScore']


    valueList=[tweetUserID,tweetText,tweetLang,tweetTimeZone,tweetDate,tweetTime,tweetLocation,tweetLatitude,tweetLongitude,tweetUserName,
                     tweetUserScreen,tweetUserUrl,tweetScore,tweetCrime,candidate,hscore,dscore]
    #print valueList
    try :
        sqlStatement = "INSERT INTO " + table_name + " ("+keyList[0]+","+keyList[1]+","+keyList[2]+","+keyList[3]+","+keyList[4]+","+keyList[5]\
              +","+keyList[6]+","+keyList[7]+","+keyList[8]+","+keyList[9]+","+keyList[10]+","+keyList[11]+","+keyList[12]+","+keyList[13]\
                  +","+keyList[14]+","+keyList[15]+","+keyList[16]+")" \
                    " VALUES ('" + str(valueList[0][row]) + "','" + str(valueList[1][row]) +"','" + str(valueList[2][row]) +"','" +'"' +str(valueList[3][row]) +'"'+\
                  "','" + str(valueList[4][row])+"','" + str(valueList[5][row])+"','" + str(valueList[6][row])+"','" + str(valueList[7][row])\
                  +"','" + str(valueList[8][row])+"','" + str(valueList[9][row])+"','" + str(valueList[10][row])+"','" + str(valueList[11][row])\
                  + "','" + str(valueList[12][row])+"','" + str(valueList[13][row])+"','" + str(valueList[14][row])+"','" + str(valueList[15][row])\
                  +"','" + str(valueList[16][row])+"')"
        #print sqlStatement
        s = cur.prepare(sqlStatement)
        cur.execute(s)
        tweetLogs.dbLogIt(sqlStatement)
    except cx_Oracle.DatabaseError as e:
        r = (("Error: Database insert Failed with message %s" % (e.message)) + " " + ("For the follwoing sql Insert Statement %s" %(sqlStatement)))
        tweetLogs.dbLogIt(r)
        print(r)
    except UnicodeEncodeError as e:
        r = (("UnicodeError: Data Unicode Error %s" % (e.message)) + " " + ("For the follwoing Insert Statement %s" %(sqlStatement)))
        tweetLogs.dbLogIt(r)
        print (r)

    con.commit()
    cur.close()
    con.close()