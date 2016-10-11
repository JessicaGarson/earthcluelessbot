import tweepy, time, sys
import os
from markovbot import MarkovBot

tweetbot = MarkovBot()

dirname = os.path.dirname(os.path.abspath(__file__))
book = os.path.join(dirname, 'Corpus.txt')
tweetbot.read(book)

CONSUMER_KEY = '7dq6VlGt7bj09pk5qIWjaD0Bq'
CONSUMER_SECRET = 'ss7bXJHwlIbKkfyLOTm07O7VivERgU9tDu4Sh4poEz8LWxgX3R'
ACCESS_KEY = '780837574013181952-fSNXikG267x3BYKpsTYDXn2k9Cs6hn9'
ACCESS_SECRET = 'Hac7W4f9ZtzXf4bUGBY2qB4Awhvw1vRvd5s1EQyHLr6Fu'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

for line in book:
    api.update_status(tweetbot.generate_text(15, seedword=['mall', 'vegan']))
    time.sleep(900) #This tweets every 15 minutes
