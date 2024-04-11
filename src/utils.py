import os
import sys
import glob
import re
import json
import datetime
from collections import Counter

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from nltk.corpus import stopwords

from loader import NewsDataLoader

def load_data(data_directory):
    loader = NewsDataLoader(data_directory)
    return loader.load_data()

def analyze_top_bottom_websites(merge_df):
    top_10_websites = merge_df['source_name'].value_counts().head(10)
    bottom_10_websites = merge_df['source_name'].value_counts().tail(10)
    return top_10_websites, bottom_10_websites

def analyze_websites_traffic(merge_df):
    websites_traffic = merge_df.groupby('source_name')['GlobalRank'].max().nlargest(10)
    return websites_traffic

def get_domain(url):
    return re.sub(r'^www.', '', re.sub(r'^https?://', '', url.split('/')[2]))


