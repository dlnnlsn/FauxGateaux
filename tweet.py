#!/usr/bin/env python3

import sys
import getopt

import credentials
import tweepy

options = getopt.getopt(sys.argv[1:], "i:t:", ["image=", "tweet="])

hasTweet = False

tweet = ""
image = ""

for option, value in options[0]:
    if option in ["-t", "--tweet"]:
        hasTweet = True
        tweet = value
    elif option in ["-i", "--image"]:
        image = value

if not hasTweet:
    tweet = input("Enter tweet: ")

auth = tweepy.OAuthHandler(consumer_key = credentials.con_key,
	consumer_secret = credentials.con_secret)

auth.set_access_token(key = credentials.token,
	secret = credentials.token_secret)

api = tweepy.API(auth)

if image:
    api.update_with_media(image, tweet)
else:
    api.update_status(tweet)

