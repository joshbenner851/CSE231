from twitter import *
import os

# put your tokens, keys, secrets, and Twitter handle in the following variables
OAUTH_TOKEN = "1649473778-1eXYWCBpikbyM6nooX7wryrNJ4CWf3OXY29GAdM"
OAUTH_SECRET = "tGfxBdsTJaetOP9sX9oQkzIndMKJ7IIlADZ9Csqy2NCjV"
CONSUMER_KEY = "3lwYLKb93hPuV3BnqTExRQUqM"
CONSUMER_SECRET = "kuHUlGDCLAOSCMIA0u2NSX8OTpIN7h1WzxzthITxcuKsdN4qsP"
TWITTER_HANDLE = ""

# put the full path and file name of the file you want to store your "already followed"
# list in

t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
            CONSUMER_KEY, CONSUMER_SECRET))

print(t.search.tweets("MSU","recent",100))
