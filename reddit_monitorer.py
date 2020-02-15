'''
Requires the creation of a praw.ini file in the same directory as this script. 
The INI file should contain the necessary credentials for the individual user 
of the script, which can be obtained by following the instructions for OAuth2
found at the following URL: 

https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps

The way this code is set up, all image files that are not *.jpg files will be 
converted, so that the code is easier to read at the end. This code currently
only works for image files (*.jpg, *.jpeg, and *.png), but if certain modifications
are made to the code, it can also be used for *.gif files.  
'''

import praw 
import requests
import random 
import string 
import os.path 
from os import path

reddit = praw.Reddit('reddit_bot')

# Enter the name of a subreddit (case sensitive)
# ex: pcmasterrace
subR = input("Please enter the name of a subreddit: \n")
subreddit = reddit.subreddit(subR)

# submission = reddit.submission(id='f3pf6c')
# print(submission.title)
# comms = list(submission.comments)
# pprint.pprint(comms[0].body)
# pprint.pprint(submission.url)
# print(dir(submission))

unfiltered_list = [sub.url for sub in subreddit.new(limit=5)]
jpgs =  list(filter(lambda x: x.endswith('.jpg'), unfiltered_list))
jpegs = list(filter(lambda x: x.endswith('.jpeg'), unfiltered_list))
pngs =  list(filter(lambda x: x.endswith('.png'), unfiltered_list))

urls = jpgs + jpegs + pngs
choose_from = [i for i in string.ascii_letters] + [str(i) for i in range(10)]
file_ext =  ".jpg"

for link in urls:
    rand_lst = [random.choice(choose_from) for _ in range(12)]
    rand_str = "".join(rand_lst)

    r = requests.get(link)
    if path.exists(f"{rand_str}{file_ext}") == False:
        with open(f"{rand_str}{file_ext}", 'wb') as f:
            f.write(r.content)
    else:
        continue

# print(reddit.read_only)
# for sub in reddit.subreddit('learnpython').hot(limit=10):
#     print(sub.title)