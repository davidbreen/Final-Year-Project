import tweepy
import sqlite3
import time
import sys
import mmap
from collections import Counter
consumer_key ='h6CFLDQq7LTAOganSnNf1dxMU'
consumer_secret='7w4tadGfTX63xy16ZnrtVMHlstLUJT9nYJ5Byz5MxAh1ATaCj8'
access_token='1573939332-5afd22LW33Ebt9MWknDJVxgorafWZjx08RVQIok'
access_secret='JhQ2jDk8GcPZBZIwUbt8IbOKbCpfCimg72KmxRHvSPxzy'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth,wait_on_rate_limit_notify = True)

conn = sqlite3.connect('C:/Users/David/Desktop/fyp/senators.db')
c = conn.cursor()

select=c.execute("SELECT Name FROM info")
every_name = select.fetchall()
newlist=[]
for i in every_name:
  if i[0] not in newlist:
    newlist.append(i[0])
i=0
count=0
for i in range(0,len(newlist)):
  try:
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=newlist[i], count=200).items(20):
        with open("C:/Users/David/Desktop/fyp//outSen.txt", "a") as text_file:
          text_file.write("Name: ")
          text_file.write(tweet.author.name.encode('utf8'))
          text_file.write("--->")
          text_file.write(tweet.text.encode('utf8'))
          text_file.write("\n")
        count+=1
        sys.stdout.flush()
        print count
        sys.stdout.flush()
  except tweepy.TweepError:
      print "Sleep 15mins"
      sys.stdout.flush()
      time.sleep(60*15)
      continue     