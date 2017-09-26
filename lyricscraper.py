#!/usr/bin/env python
# -*- coding: utf-8 -*-
# lyricscraper.py - scrapes Joyce Manor lyrics from web
from bs4 import BeautifulSoup
import requests
import sys

# with open('urls.txt') as f:
# 	urls = (line.strip() for line in f)
# 	for url in urls:
# Pretty sure my IP got blacklisted, so this doesn't seem to work?
url = 'http://www.plyrics.com/lyrics/joycemanor/christmascard.html'
headers = {
    'User-Agent': 'X11; U; Linux x86_64; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3'}
# Get the webpage and create response object
response = requests.get(url, headers=headers)

try:
    response.raise_for_status()
except Exception as e:
    print(e)
    exit()

# Pass extracted source (response) to bs4
soup = BeautifulSoup(response.text, "lxml")

# Extract URLs
for lyrics in soup.find_all("div", {"class": "content_lyr"}):
    print lyrics
# f.close()
