#!/usr/bin/env python
# -*- coding: utf-8 -*-
# lyricscraper.py - scrapes Joyce Manor lyrics from web
from bs4 import BeautifulSoup
import requests

url = 'https://www.songlyrics.com/joyce-manor-lyrics/' 

# get the webpage and create response object
response = requests.get(url)

# pass extracted source (response) to bs4 
soup = BeautifulSoup(response.text, "lxml")

# Extracting URLs from the attribute href in the <a> tags.
for tag in soup.find_all(class_ = "tracklist"):
    

# songs = []

# for tag in soup.select('a'):
#    link = "http://www.plyrics.com/" + tag.get('href')
#    songs.append(link)
    
# print songs