import praw
import pdb
import re
import os

#Create instance, Logged in via praw.ini
reddit = praw.Reddit('bot1')

#make posts_replied_to list or read posts_replied_to list from file
if not os.path.isfile("posts_relied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_relied_to.txt","r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))
        
subreddit = reddit.subreddit("pythonforengineers")  #test reddit, otherwise would be dota2

for submission in subreddit.hot(limit=5):
    if submission.id not in posts_replied_to:
        if re.search("wow", submission.title, re.IGNORECASE):
            submission.reply("WAOW! \n I am a bot.")
            print("Bot replying to: ", submission.title)
            posts_replied_to.append(submission.id)
            
with open("posts_relied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")