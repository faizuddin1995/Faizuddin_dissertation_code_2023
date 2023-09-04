import pandas as pd
from tqdm.notebook import tqdm
import snscrape.modules.twitter as sntwitter

scraper = sntwitter.TwitterSearchScraper("#lucidmotors")
tweets = []
n_tweet=10000
for i, tweet in tqdm(enumerate(scraper.get_items()), total = n_tweet):
    data = [
        tweet.date,
        tweet.id,
        tweet.content,
        tweet.user.username,
        tweet.likeCount,
        tweet.retweetCount,
    ]
    tweets.append(data)
    if i > n_tweet:
        break

tweet_df = pd.DataFrame(tweets, columns=["date", "id", "content", "username", "like_count", "retweet_count"])

tweet_df.to_csv("D:/Pdownload/sentimenttweet/lucidmotors_tweets.csv", index=False)
