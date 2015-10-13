import tweepy

consumer_key ='h6CFLDQq7LTAOganSnNf1dxMU'
consumer_secret='7w4tadGfTX63xy16ZnrtVMHlstLUJT9nYJ5Byz5MxAh1ATaCj8'
access_token='1573939332-5afd22LW33Ebt9MWknDJVxgorafWZjx08RVQIok'
access_secret='JhQ2jDk8GcPZBZIwUbt8IbOKbCpfCimg72KmxRHvSPxzy'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

'''
members = api.list_members(screen_name='ballsdotie',slug='Irish rugby players')
for user in members:
    print user.screen_name
'''

for member in tweepy.Cursor(api.list_members, 'ballsdotie', 'Irish rugby players').items():
    print member.screen_name