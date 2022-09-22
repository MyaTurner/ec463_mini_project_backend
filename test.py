from turtle import pd
import tweepy
import sys

auth = tweepy.OAuthHandler('yHZb59eSuL0nLa9p3mXmhvfXY', 'fwnl9jvmZ8zHQkmkn0voIBhaXwu9RayPF01eA0WuNW3MCGZcbO')
auth.set_access_token('1569786813157613568-RlvY9b2OwZS7iVPyIeFucVvVw5afrh','tG4NO0GDuc02R26II9eLejVxjtVZ1rNnPbLncj10tA5ws')
api = tweepy.API(auth)

def get_related_tweets(key_word):
    
    twitter_users = []
    tweet_string = [] 
    
    for tweet in tweepy.Cursor(api.search_tweets,q=key_word, count=1000).items(10000):
            # Analyzing only original tweets, no retweets
            if (not tweet.retweeted) and ('RT @' not in tweet.text):
                # Filter to only english tweets
                if tweet.lang == "en":
                    # Tweeter's username 
                    twitter_users.append(tweet.user.name)
                    # Their tweet
                    tweet_string.append(tweet.text)
                    print([tweet.user.name,tweet.text])
    df = pd.DataFrame({'name':twitter_users, 'tweet': tweet_string})
    return df

def main():
    get_related_tweets("food")
if __name__ == '__main__':
    main()