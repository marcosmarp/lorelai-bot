from functions import RunBot, InitPraw, sleep, stderr
from traceback import print_exc

reddit_handler = InitPraw()
gilmoregirls_subreddit_handler = reddit_handler.subreddit("gilmoregirls")
test_subreddit_handler = reddit_handler.subreddit("lorelaibot")

while(True):
  try:
    RunBot(gilmoregirls_subreddit_handler)
  except KeyboardInterrupt: # For quitting with ctrl+C
    break
  except:
    print("Reddit exception: ", file=stderr)
    print_exc()

