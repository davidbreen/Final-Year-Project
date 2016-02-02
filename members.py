import tweepy
import sqlite3

consumer_key ='h6CFLDQq7LTAOganSnNf1dxMU'
consumer_secret='7w4tadGfTX63xy16ZnrtVMHlstLUJT9nYJ5Byz5MxAh1ATaCj8'
access_token='1573939332-5afd22LW33Ebt9MWknDJVxgorafWZjx08RVQIok'
access_secret='JhQ2jDk8GcPZBZIwUbt8IbOKbCpfCimg72KmxRHvSPxzy'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

conn = sqlite3.connect('example5.db')
c = conn.cursor()
c.execute('''DROP TABLE rugby''')
c.execute('''CREATE TABLE rugby
          (Name)''')

for member in tweepy.Cursor(api.list_members, 'ballsdotie', 'irish-rugby-players').items():
    temp1=member.screen_name
    temp2 = [(temp1)]
    c.executemany("INSERT INTO rugby(Name) VALUES (?);" , (temp2,))
    conn.commit()

conn.close()
