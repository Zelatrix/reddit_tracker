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
from pathlib import Path

import os.path 
from os import path

# Creating a new Reddit instance to access the API
reddit = praw.Reddit('reddit_bot')

'''
Allows for multiple subreddits to be entered. Enter each 
subreddit followed by the enter key
''' 
def exec(n):
    subR = ""
    for i in range(n, 0, -1):
        if not (i == 1):
            inp = input(f"Please enter the names of {i} subreddits: \n")
            subR += (inp + "+")
        else:
            inp = input(f"Please enter the name of {i} subreddit: \n")
            subR += inp
    print("Monitoring subreddits...")
    return subR

'''
Filtering out all the individual image types from the full
list of extracted items. 
'''
def create_url_stream(subreddit):
    # unfiltered_list = [sub.url for sub in subreddit.new(limit=5)] # subreddit.stream.submissions()]
    # urls = []
    # for sub in subreddit.new(limit=None): 
    for sub in subreddit.stream.submissions():
        # # only_jpgs = filter(lambda x: lambda x: x.endswith('.jpg'), subreddit.stream.submissions())
        if (str(sub.url).endswith(('.jpg', '.jpeg', '.png'))):
        # urls.append(sub.url)
    # return urls
            # return sub.url
            # print(sub.url)
            download_img(sub.url, '.jpg')

    # jpgs =  list(filter(lambda x: x.endswith('.jpg'), unfiltered_list))    # A list containing only *.jpg files
    # jpegs = list(filter(lambda x: x.endswith('.jpeg'), unfiltered_list))   # A list containing only *.jpeg files
    # pngs =  list(filter(lambda x: x.endswith('.png'), unfiltered_list))    # A list containing only *.png files

    # urls = jpgs + jpegs + pngs
    # return urls
    
'''
For this piece of code to function properly, a folder must be created 
inside the same directory as the script to store the files in, as the 
location that is used for output is a relative path
'''
def download_img(url, file_ext):
    choose_from = [i for i in string.ascii_letters] + [str(i) for i in range(10)]

    # for link in urls:
    rand_lst = [random.choice(choose_from) for _ in range(12)]
    rand_str = "".join(rand_lst)
    location = Path.cwd()/f"output_pics"/f"{rand_str}{file_ext}"

    # Send a request to the image URL that has been grabbed using the API
    # If the filename that is to be assigned to a file does not already exist,
    # create the file with that name, otherwise, skip that filename and generate
    # a new one.
    r = requests.get(url)
    if path.exists(location) == False:
        with open(location, 'wb') as f:
            f.write(r.content)
            f.close()
            print("Image saved!")
    # else:
        # continue

def main():
    n = int(input("How many subreddits would you like to search? \n"))
    subreddit = reddit.subreddit(exec(n))
    
    create_url_stream(subreddit)
    # for img in urls:
    #     download_img(img, '.jpg')
    #     # download_img(img, '.jpeg')
    #     # download_img(img, '.png')

if __name__ == "__main__":
    main()
