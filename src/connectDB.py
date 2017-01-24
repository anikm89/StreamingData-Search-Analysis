import cx_Oracle
import logging
import tweetLogs

k = []
l = []

def insertIntoDB(tweetdict):
    for key, value in tweetdict.items():
        k.append(key)
        l.append(value)
        #print l
    dbConnection(k, l)

def dbConnection(keyList,valueList):
    con = cx_Oracle.connect('admin/admin@localhost/xe')
    cur = con.cursor()
    table_name = "TWITTER_DATA_TABLE"
    for i in range(len(valueList[0])):
        try :
            sqlcode = "INSERT INTO " + table_name + " ("+keyList[0]+","+keyList[1]+","+keyList[2]+","+keyList[3]+","+keyList[4]+","+keyList[5]\
                  +","+keyList[6]+","+keyList[7]+","+keyList[8]+","+keyList[9]+","+keyList[10]+","+keyList[11]+","+keyList[12]+","+keyList[13]+","+keyList[14]+")" \
                        " VALUES ('" + str(valueList[0][i]) + "','" + str(valueList[1][i]) +"','" + str(valueList[2][i]) +"','" +'"' +str(valueList[3][i]) +'"'+\
                      "','" + str(valueList[4][i])+"','" + str(valueList[5][i])+"','" + str(valueList[6][i])+"','" + str(valueList[7][i])\
                      +"','" + str(valueList[8][i])+"','" + str(valueList[9][i])+"','" + str(valueList[10][i])+"','" + str(valueList[11][i]) + "','" + str(valueList[12][i])+"','" + str(valueList[13][i])+"','" + str(valueList[14][i])+"')"
            #print sqlcode
            s = cur.prepare(sqlcode)
            cur.execute(s)
        except cx_Oracle.DatabaseError as e:
            r = (("Error: Database insert Failed with message %s" % (e.message)) + " " + ("For the follwoing sql Insert Statement %s" %(sqlcode)))
            tweetLogs.logIt(r)
            print(r)
        except UnicodeEncodeError as e:
            r = (("UnicodeError: Data Unicode Error %s" % (e.message)) + " " + ("For the follwoing Insert Statement %s" %(sqlcode)))
            tweetLogs.logIt(r)
            print (r)

        con.commit()

    cur.close()
    con.close()