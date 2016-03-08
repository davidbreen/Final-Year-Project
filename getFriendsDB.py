import tweepy
import sqlite3
import time
import sys

consumer_key ='h6CFLDQq7LTAOganSnNf1dxMU'
consumer_secret='7w4tadGfTX63xy16ZnrtVMHlstLUJT9nYJ5Byz5MxAh1ATaCj8'
access_token='1573939332-5afd22LW33Ebt9MWknDJVxgorafWZjx08RVQIok'
access_secret='JhQ2jDk8GcPZBZIwUbt8IbOKbCpfCimg72KmxRHvSPxzy'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth,wait_on_rate_limit_notify = True)

conn = sqlite3.connect('C:/Users/David/Desktop/fyp/senators.db')
c = conn.cursor()
#c.execute('''DROP TABLE info''')
c.execute('''CREATE TABLE info
          (Name, Friend)''')

for page in tweepy.Cursor(api.list_members, 'cspan', 'senators', count=200).items():
    temp1=page.screen_name
    print temp1
    sys.stdout.flush()
    i=0      
    try:
        for friend in tweepy.Cursor(api.friends, screen_name =temp1, count=200).items():
            print i
            sys.stdout.flush()
            i=i+1
            u=friend.screen_name
            temp3=[temp1,u]
            c.executemany("INSERT INTO info(Name, Friend) VALUES (?, ?);", [temp3])
            conn.commit()
    except tweepy.TweepError:
        print "Sleep 15mins"
        sys.stdout.flush()
        time.sleep(60*15)
        continue
 

conn.close()
