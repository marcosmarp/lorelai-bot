from datetime import datetime
from time import sleep
from praw import Reddit
from os import environ
from random import randint
import pytz
from sys import stderr

def InitPraw():
  return Reddit(
    client_id = environ['CLIENT_ID'],
    client_secret = environ['CLIENT_SECRET'],
    user_agent="console:lorelai-bot:v1.0.0 (by u/doctor-who-bot)",
    username = "lorelai-bot",
    password = environ['PASSWORD']
  )

def LoadQuotes():
  quotes = []
  file = open('quotes.txt', 'r', encoding='utf-8')
  for line in file:
    quotes.append(line)
  file.close()
  return quotes

def AlreadyReplied(replies):
  for reply in replies:
    if reply.author.name == "lorelai-bot":
      return True
  return False

def GetRandomPositionOfObject(object):
  return randint(0, len(object)-1)

def PostHaveComments(post):
  return (post.num_comments > 0)

def ReplyRandomQuote(comment):
  quotes = LoadQuotes()
  random_quote_position = GetRandomPositionOfObject(quotes)
  reply = quotes[random_quote_position] + "\n" + "^(I'm a bot and this was a Lorelai Gilmore quote. Upvote me to keep me running!)" + "\n" + "\n" + "^(Feedback? Bugs? )[^(Contact the developer)](mailto:marcosmartinezpalermo@gmail.com)" + "\n" + "\n" "[^(Github)](https://github.com/marcosmarp/lorelai-bot)"
  comment.reply(reply)
  return quotes[random_quote_position]

def StoreReply(comment, reply):
  amount_of_lines = 0
  with open("replies.txt", "r", encoding='utf-8') as file_object:
    for line in file_object:
      amount_of_lines += 1
    file_object.close()
  with open("replies.txt", "a", encoding='utf-8') as file_object:
    file_object.write("Reply #" + str(int(amount_of_lines/11 + 1)))
    file_object.write("\n")
    file_object.write(" Replied comment data:")
    file_object.write("\n")
    file_object.write("   Author: " + comment.author.name)
    file_object.write("\n")
    file_object.write("   Link: https://www.reddit.com" + comment.permalink)
    file_object.write("\n")
    file_object.write("   Post:")
    file_object.write("\n")
    file_object.write("     Title: " + comment.submission.title)
    file_object.write("\n")
    file_object.write("     Author: " + comment.submission.author.name)
    file_object.write("\n")
    file_object.write("     Link: https://www.reddit.com" + comment.submission.permalink)
    file_object.write("\n")
    file_object.write(" Reply data:")
    file_object.write("\n")
    file_object.write("   Replied quote: " + reply)
    file_object.write("\n")

def InformReplyOnScreen(comment, reply):
  now = datetime.now(pytz.timezone('America/Argentina/Buenos_Aires'))
  dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
  print(dt_string + ": replied " + comment.author.name + "'s comment with: ", file=stderr)
  print("   " + reply, file=stderr)

def CheckNewPosts(posts):
  for post in posts:
    if PostHaveComments(post):
      for comment in post.comments:
        if hasattr(comment, "body"):
          if "lorelai" in comment.body.lower():
            if not AlreadyReplied(comment.replies):
              quote_replied = ReplyRandomQuote(comment)
              InformReplyOnScreen(comment, quote_replied)
              StoreReply(comment, quote_replied)
              sleep(600)


def RunBot(subreddit_handler):
 CheckNewPosts(subreddit_handler.new(limit=10))
