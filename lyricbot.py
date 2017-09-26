#!/usr/bin/env python
# -*- coding: utf-8 -*-
# lyric_bot.py - Pulls lyrics from lyrics.txt and tweets once every 30 minutes
import tweepy, time, sys

# Twitter API credentials
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

# Grant access to API and file input
try:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
except Exception as e:
    print 'Authentication Failed: ' + e
    exit()

lyrics_file = open('lyrics.txt', 'r')
lyrics_list = []

# Parse lyrics_file
for line in lyrics_file:
    lyric = line.strip('\n')
    lyrics_list.append(lyric)
lyrics_file.close()

for lyric in lyrics_list:
    try:
        # Twitter character limit
        if ((len(lyric) + 1) <= 140):
            tweet = lyric

        # Tweet and log
        api.update_status(tweet)
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " u'\u2014' " + tweet)
        lyrics_list.remove(lyric) # don't want repeats
        time.sleep(1800) # possibly change to every 4 hrs to keep things fresh
    except tweepy.TweepError as e:
        print(e.reason)

# Overwrites scraped lyrics.txt; might not be necessary
lyrics_file = open('lyrics.txt', 'w') 
for lyric in lyrics_list:
    lyrics_file.write(lyric + "\n")
lyrics_file.close()
