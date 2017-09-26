#!/usr/bin/env python
# -*- coding: utf-8 -*-
from string import punctuation

titles = """Constant Nothing
Done Right Discount Flooring
Five Beer Plan
Chumped
Leather Jacket
Holiday Heart
D.F.H.P?
My Elise
Orange Julius
Call Out (Laundry)
Beach Community
Derailed
Famous Friend
Leather Jacket
21st Dead Rats
Constant Nothing
Ashtray Petting Zoo
Constant Headache
These Kind Of Ice Skates
Comfortable Clothes
See How Tame I Can Be
Drainage
Video Killed The Radio Star
If I Needed You There
Bride Of Usher
Violent Inside
I'm Always Tired
Christmas Card
Falling In Love Again
End Of The Summer
Victoria
Schley
Heart Tattoo
The Jerk
In The Army Now
Catalina Fight Song
Heated Swimming Pool
Fake I.D.
Eighteen
Angel In The Snow
Do You Really Want To Not Get Better?
Last You Heard Of Me
Make Me Dumb
Over Before It Began
Reversing Machine
Stairs
This Song Is A Mess But So Am I
Midnight Service At The Mutter Museum"""

no_punct = ""  
for char in titles:  
   if char not in punctuation:  
       no_punct += char  
formatted_titles = no_punct.lower().replace(" ", "")
with open('urls.txt', 'a') as f:
    f.write(formatted_titles)

with open('urls.txt', 'r+') as f:
    song_list = [line.rstrip('\n') for line in f]

with open('urls.txt', 'w') as f:
	for i in song_list:
		links = "https://www.plyrics.com/j/joycemanor/{}.html".format(i)
		# print links
		f.write(links + "\n")
f.close()

