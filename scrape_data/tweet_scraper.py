import os
import pandas as pd
import snscrape.modules.twitter as sntwitter

# Creating list to append tweet data 
tweets_list1 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('bus from:cta').get_items()): #declare a username 
    if i>100000: #number of tweets you want to scrape
        break
    tweets_list1.append([tweet.date, tweet.content, tweet.quoteCount, tweet.likeCount, tweet.retweetCount]) #declare the attributes to be returned
    
# Creating a dataframe from the tweets list above 
tweets_df = pd.DataFrame(tweets_list1, columns=['Datetime', 'Text', 'Quotes', 'Likes', 'Retweets'])

print(tweets_df)

tweets_df.to_csv('data_output/busTweets.csv')