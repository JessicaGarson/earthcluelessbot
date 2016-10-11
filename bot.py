import tweepy, time, sys
import os
from markovbot import MarkovBot

tweetbot = MarkovBot()

dirname = os.path.dirname(os.path.abspath(__file__))
book = os.path.join(dirname, 'Corpus.txt')
tweetbot.read(book)

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

for line in book:
    api.update_status(tweetbot.generate_text(15, seedword=['mall', 'vegan']))
    time.sleep(900) #This tweets every 15 minutes
