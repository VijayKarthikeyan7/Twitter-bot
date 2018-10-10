import tweepy as tp
import time
import os

#Credentials to be filled up
#write your's consumer key and all
consumer_key = "___"
consumer_secret = "____"
access_token = "___"
access_secret = "___"

#Logging in
auth = tp.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tp.API(auth)

#Tweeting images
os.chdir('parrots')
for model_image in os.listdir('.'):
    #tweeting
    api.update_with_media(model_image)
    #interval to wait for tweeting another image
    time.sleep(10)
