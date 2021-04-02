import tweepy
import time

auth = tweepy.OAuthHandler("W5QG0YHF33udZbgkXUWKcR5dT", "wIJteRKUVGlAmvXpN60go0ym4GCcdpx0M4AmoYMNibdtN6mrg5")
auth.set_access_token("1292444629-zscLtnFoEY0d8tvJCG0MzT6JmbWrSCESP5ViH5X", "Myqi0l4jrrpzDrsfMKhs9KPEmClQXTBoI975UjkyOBqgj")

api = tweepy.API(auth)
user = api.me()
# print(user.screen_name)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

def limit_handle(cursor):
  try:
    while True:
      yield cursor.next()
  except tweepy.RateLimitError:
    time.sleep(1000)

# Liking Tweets
search_string = "python"
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
  try:
    tweet.favorite()
    print("I liked that tweet!")
  except tweepy.TweepError as e:
    print(e.reason)
  except StopIteration:
    break
















# Genrous Bot (follows back all your followers)
# for follower in limit_handle(tweepy.Cursor(api.followers).items()):
  # to follow someone
  # if follower.name == "follower name":
  #   follower.follow()
  # print(follower.name)


