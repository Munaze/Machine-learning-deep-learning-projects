import tweepy
from textblob import TextBlob
Consumer_key = 'YE0jC2ebri2j27E3Q3LZlkgqt'

Consumer_Secret = 'fCdkmccgFM32wK4b41b19dt4RIQeVgR1LW7AmwFx1qSsTTMsNx'
Access_token= '849688736841576457-bkwTWoB8KGFlQpyfAVGZ1T0TE6hK0lL'
Access_token_Secret = 'UGJa38oUGLOrfTLblrOa71FLWAlufipn9eHCmU518y4V6'

auth = tweepy.OAuthHandler(Consumer_key,Consumer_Secret)
auth.set_access_token(Access_token,Access_token_Secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    
a = input(" press Enter to Exit")
