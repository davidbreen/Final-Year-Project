import tweepy
import time

consumer_key ='h6CFLDQq7LTAOganSnNf1dxMU'
consumer_secret='7w4tadGfTX63xy16ZnrtVMHlstLUJT9nYJ5Byz5MxAh1ATaCj8'
access_token='1573939332-5afd22LW33Ebt9MWknDJVxgorafWZjx08RVQIok'
access_secret='JhQ2jDk8GcPZBZIwUbt8IbOKbCpfCimg72KmxRHvSPxzy'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

list= open('C:/Users/David/Desktop/twitter_followers.txt','w')

user = tweepy.Cursor(api.followers, screen_name="SeanCronin2").items()
    
while True:
    try:
        u = next(user)
        list.write(u.screen_name +' \n')

    except:
        print 'End after 1 minute, results printed into text file'
        time.sleep(1*60)
        u = next(user)
        list.write(u.screen_name +' \n')
list.close()