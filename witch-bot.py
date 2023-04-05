import praw
import re
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.environ.get("REDDIT_CLIENT_ID")
client_secret = os.environ.get("REDDIT_CLIENT_SECRET")
username = os.environ.get("REDDIT_USERNAME")
password = os.environ.get("REDDIT_PASSWORD")
user_agent = os.environ.get("REDDIT_USER_AGENT")

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)

print("brrrrrrr")
subreddit = reddit.subreddit("developersIndia")

for comment in subreddit.stream.comments(skip_existing=True):
    if re.search(r"\bwhat\s+is\s+witch\b", comment.body, re.IGNORECASE):
        comment.reply("WIPRO - INFOSYS - TCS - COGNIZANT - HCL")
