# -*- coding: utf-8 -*-


#File authorization from google drive
from google.colab import drive
drive.mount('/content/drive')

#importing twitter data set
import pandas as pd
DATASET_COLUMNS = ['date','id','content','like_count','retweet_count','sentiment_category','sentiment_numeric']
path = '/content/drive/MyDrive/data/new/tweets_with_sentiment.csv'
df = pd.read_csv(path, encoding='ISO-8859-1', on_bad_lines='skip', names = DATASET_COLUMNS)

import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Create a new DataFrame with selected columns
new_df = df[['date', 'content', 'sentiment_numeric']].copy()

# Handle missing values in the new DataFrame
new_df['content'].fillna('', inplace=True)

# Text cleaning and preprocessing
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

# Apply preprocessing to "content" column
new_df['content'] = new_df['content'].apply(lambda x: re.sub(r'[^\w\s]', '', x))
new_df['content'] = new_df['content'].str.lower()
new_df['content'] = new_df['content'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))
new_df['content'] = new_df['content'].apply(lambda x: ' '.join([stemmer.stem(word) for word in x.split()]))

# Save the cleaned DataFrame to a new CSV file
new_df.to_csv('/content/drive/MyDrive/data/new/cleaned_tweet_data.csv', index=False)
