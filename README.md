# reddit_tracker

Requires the creation of a ``praw.ini`` file in the same directory as this script. 
The INI file should contain the necessary credentials for the individual user 
of the script, which can be obtained by following the instructions for OAuth2
found at the following URL: 

https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps

The way this code is set up, all image files that are not ``\*.jpg`` files will be 
converted, so that the code is easier to read at the end. This code currently
only works for image files (``\*.jpg``, ``\*.jpeg``, and ``\*.png``), but if certain modifications
are made to the code, it can also be used for ``\*.gif`` files.
