import tweepy

auth = tweepy.OAuthHandler("W5QG0YHF33udZbgkXUWKcR5dT", "wIJteRKUVGlAmvXpN60go0ym4GCcdpx0M4AmoYMNibdtN6mrg5")
auth.set_access_token("1292444629-zscLtnFoEY0d8tvJCG0MzT6JmbWrSCESP5ViH5X", "Myqi0l4jrrpzDrsfMKhs9KPEmClQXTBoI975UjkyOBqgj")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

