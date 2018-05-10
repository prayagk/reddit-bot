import praw
import time

def connection():
	reddit = praw.Reddit(username = "Your reddit username",
			                 password = "Your reddit password",
			                 client_id = "bot client id",
			                 client_secret = "bot client secret",
			                 user_agent = "bot name")
	print "Connection established"

	return reddit

def botAction(reddit):
	for comment in reddit.subreddit('bitcoin').hot(limit=25)
	  print comment.author
  
  time.sleep(10)

reddit = connection()

while True:
	botAction(reddit)
