import tweepy
import time
import sqlite3

consumer_key ='h6CFLDQq7LTAOganSnNf1dxMU'
consumer_secret='7w4tadGfTX63xy16ZnrtVMHlstLUJT9nYJ5Byz5MxAh1ATaCj8'
access_token='1573939332-5afd22LW33Ebt9MWknDJVxgorafWZjx08RVQIok'
access_secret='JhQ2jDk8GcPZBZIwUbt8IbOKbCpfCimg72KmxRHvSPxzy'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

list= open('C:/Users/David/Desktop/twitter_friends.txt','w')

with open('C:/Users/David/Desktop/5_rugby_list.txt') as f:
    player = f.readlines()
    
i=0
while i<len(player):
    user = tweepy.Cursor(api.friends, screen_name=player[i]).items()
    list.write("\nFriends of %s \n" % player[i])
    k=0
    while True:       
        try:
            u = next(user)
            list.write(u.screen_name +' \n')
            k+=1
        except:
            print 'End due to time limit'
            time.sleep(15*60)
            continue
    i+=1
list.close()

    