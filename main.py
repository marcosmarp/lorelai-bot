from functions import RunBot, InitPraw, sleep

reddit_handler = InitPraw()
doctor_who_subreddit_handler = reddit_handler.subreddit("gilmoregirls")

while(True):
  RunBot(doctor_who_subreddit_handler)
