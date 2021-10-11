from functions import RunBot, InitPraw, sleep

reddit_handler = InitPraw()
gilmoregirls_subreddit_handler = reddit_handler.subreddit("gilmoregirls")
test_subreddit_handler = reddit_handler.subreddit("lorelaibot")

while(True):
  RunBot(gilmoregirls_subreddit_handler)
