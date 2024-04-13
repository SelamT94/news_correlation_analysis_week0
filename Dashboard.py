
import os
from tkinter import Image
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

rating_df=pd.read_csv("./data/rating.csv")
domain_locations_df = pd.read_csv("./data/domains_location.csv")
traffic_data_df = pd.read_csv("./data/traffic.csv")

# S# Title
st.title("Global News Analytics Dashboard")

# Sidebar (optional)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "EDA", "Sentiment Analysis", "Topic Modeling"])


# Page Content
if page == "Home":
    st.title("Welcome to the Global News Analytics Dashboard")
    st.markdown("Explore insights and trends in global news data.")
    
    st.markdown("---")
    
    st.write("This dashboard provides a comprehensive analysis of global news data, including article counts by source, website traffic distribution, sentiment analysis, and more. Use the navigation on the left to explore different sections.")
    
    st.write("Get started by selecting a section from the sidebar on the left.")
    
    st.markdown("---")
    
elif page == "EDA":
    st.write("## Exploratory Data Analysis")

    st.write("### Top 10 Websites")
    top_10_websites = rating_df['source_name'].value_counts().head(10)
    st.bar_chart(top_10_websites)
    
    st.write("### Article Counts by Source")
    article_counts_by_source = rating_df['source_name'].value_counts()
    st.bar_chart(article_counts_by_source.head(10))
    st.write("This chart shows the distribution of articles by source.")

    # Website Traffic Distribution
    st.write("### Website Traffic Distribution")
    plt.hist(traffic_data_df['GlobalRank'], bins=30)
    st.pyplot()
    st.write("This histogram displays the distribution of website traffic ranks.")
    
    

elif page == "Sentiment Analysis":
    # Sentiment Analysis
    st.write("## Sentiment Analysis")
    # Sentiment Analysis Distribution
    st.write("### Sentiment Analysis Distribution")
    sentiment_counts = rating_df['title_sentiment'].value_counts()
    st.bar_chart(sentiment_counts)
    st.write("This bar chart illustrates the distribution of sentiment categories.")

    # Include your sentiment analysis visualizations here

elif page == "Topic Modeling":
    # Topic Modeling
    st.write("## Topic Modeling")
    # screenshot_folder = "./screenshot"
    # image_path = os.path.join(screenshot_folder, "Topic_modeling.png")
    # st.image(image_path, caption='Topic Modeling Plot')
    # Include your topic modeling visualizations here





