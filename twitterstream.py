from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'h6CFLDQq7LTAOganSnNf1dxMU'
csecret = '7w4tadGfTX63xy16ZnrtVMHlstLUJT9nYJ5Byz5MxAh1ATaCj8'
atoken = '1573939332-5afd22LW33Ebt9MWknDJVxgorafWZjx08RVQIok'
asecret = 'JhQ2jDk8GcPZBZIwUbt8IbOKbCpfCimg72KmxRHvSPxzy'

class listener(StreamListener):

	def on_data(self, data):
		print data
		return True
		
	def on_error(self, status):
		print status
		
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["progressives"])