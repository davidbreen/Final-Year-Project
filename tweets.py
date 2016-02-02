import tweepy
import sqlite3
import time
import sys
from collections import Counter
consumer_key ='h6CFLDQq7LTAOganSnNf1dxMU'
consumer_secret='7w4tadGfTX63xy16ZnrtVMHlstLUJT9nYJ5Byz5MxAh1ATaCj8'
access_token='1573939332-5afd22LW33Ebt9MWknDJVxgorafWZjx08RVQIok'
access_secret='JhQ2jDk8GcPZBZIwUbt8IbOKbCpfCimg72KmxRHvSPxzy'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth,wait_on_rate_limit_notify = True)

conn = sqlite3.connect('C:/Users/David/Desktop/fyp/presidents.db')
c = conn.cursor()

select=c.execute("SELECT Name FROM info")
every_name = select.fetchall()
newlist=[]
for i in every_name:
  if i[0] not in newlist:
    newlist.append(i[0])
p=0
i=0
hashtags = []
for i in range(0,1):
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=newlist[i]).items():
        #temp= item.entities.get('hashtags')
        #hashtags.append(temp)
        #print hashtags
        print "Name:", tweet.author.name.encode('utf8')
        print "Screen-name:", tweet.author.screen_name.encode('utf8')
        print "Tweet created:", tweet.created_at
        print "Tweet:", tweet.text.encode('utf8')
        print "Hashtag:", tweet.entities.get('hashtags')
        print "Mentions:", tweet.entities.get('user_mentions')
        print "Retweeted:", tweet.retweeted
        print "Favourited:", tweet.favorited
        print "Location:", tweet.user.location.encode('utf8')
        print "Time-zone:", tweet.user.time_zone
        print "Geo:", tweet.geo
        print "//////////////////"

#count = Counter([d['text'] for d in hashtags])
#print(count.most_common())