import json
import argparse
import os
import glob
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime

#Loading all the datas

rating=pd.read_csv("./data/rating.csv")
domain_locations = pd.read_csv("./data/domains_location.csv")
traffic_data = pd.read_csv("./data/traffic.csv")


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
          

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Export News history')

    
    parser.add_argument('--zip', help="Name of a zip file to import")
    args = parser.parse_args()

loader=NewsDataLoader("rating")