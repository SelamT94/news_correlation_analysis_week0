import json
import argparse
import os, re
import glob
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Create wrapper classes for using news_sdk 
class NewsDataLoader:
    '''
    News exported data IO class.
    When you open news exported ZIP file, you will find a rating csv fill which will contain data from the 
    news articles.    
    '''
    def __init__(self, path):
        '''
        path: path to the news exported data folder
        '''
        self.path = path
          

    def load_data(self):

        #Loading all the datas into a shared dataframe

        rating_df=pd.read_csv("../data/rating.csv")
        domain_locations_df = pd.read_csv("../data/domains_location.csv")
        traffic_data_df = pd.read_csv("../data/traffic.csv")
        merge_df=pd.merge(rating_df, domain_locations_df ,left_on='source_name', right_on ='SourceCommonName' ,how ='left')
        merge_df=pd.merge(merge_df, traffic_data_df , left_on ='source_name' ,right_on='Domain' ,how ='left')
        # print(merge_df.columns)
        return(merge_df)
    
    def analyze_data(self, data):
    
        #  Calculate descriptive statistics
        descriptive_stats = data.describe()

        mean_sentiment = data['title_sentiment'].mean()
        median_sentiment = data['title_sentiment'].median()
        max_views = data['GlobalRank'].max()

        analysis_result = {
            'descriptive_statistics': descriptive_stats,
            'mean_sentiment': mean_sentiment,
            'median_sentiment': median_sentiment,
            'max_views': max_views
        }

        return analysis_result

    def preprocess_text(self, text_column):
        """
        Preprocesses news data.
        """

        stop_words = set(stopwords.words('english'))
        ps = PorterStemmer()

        preprocessed_text = []

        for text in text_column:
            text = text.lower()

            # Remove non-alphanumeric characters and punctuation
            text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

            tokens = word_tokenize(text)
            filtered_tokens = [ps.stem(word) for word in tokens if word not in stop_words]
            preprocessed_text.append(' '.join(filtered_tokens))

        return pd.Series(preprocessed_text)

if __name__ == "__main__":
    # Initialize NewsDataLoader with the correct data directory path
    data_directory = "../data"  
    loader = NewsDataLoader(data_directory)

    data = loader.load_data()
    
    analysis_result = loader.analyze_data(data)
    print(analysis_result)

    preprocessed_description = loader.preprocess_text(data['description'])
    print(preprocessed_description.head())
