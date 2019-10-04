from twython import Twython, TwythonError
import json
import sys

CREDENTIALS_FILENAME = 'creds.json'
jf = open(CREDENTIALS_FILENAME)
creds = json.load(jf)
jf.close()

def default_function():
	twitter = Twython(creds['consumer_key'], creds['consumer_secret'])
	tweets = []
	try:
		user_timeline = twitter.get_user_timeline(screen_name='iitbbs',count=30)
	except TwythonError as e:
		print(e)

	# Version check for python 2 compliance
	for tweet in user_timeline:
		# Add whatever you want from the tweet, here we just add the text
		res = {}
		if int(sys.version[0]) == 2:
			res['text'] = tweet['text'].encode('utf-8')
		else:
			res['text'] = tweet['text']
		#res['text'] = str(tweet['text'])
		if len(tweet['entities']['urls']) != 0:
			if int(sys.version[0]) == 2:
				res['url'] = tweet['entities']['urls'][0]['expanded_url'].encode('utf-8')
			else:
				res['url'] = tweet['entities']['urls'][0]['expanded_url']
			res['text'] = res['text'][0:tweet['entities']['urls'][0]['indices'][0]]
		else:
			res['url'] = "No link for this tweet"
		tweets.append(res)
	
	return tweets