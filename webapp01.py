from PIL import Image

#https://medium.com/pythoneers/word-cloud-app-with-streamlit-framework-in-python-4b9b440d485
import streamlit as st
import pandas as pd
import requests
!pip install "bs4"
from bs4 import BeautifulSoup
import re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


image01 = Image.open('desenvolvimento.jpg')

st.title('Simple Streamlit App')
st. markdown("""
This app performs Word Cloud
* **Python libraries:** streamlit, pandas BeautifulSoup, Wordcloud..
""")
st.set_option('deprecation.showPyplotGlobalUse', False)
st.sidebar.header("Select Link")
links = ["https://seaportai.com/blog-predictive-maintenance/",
         "https://seaportai.com/healthcare-analytics/",
         "https://seaportai.com/blog-rpameetsai/",
         "https://seaportai.com/covid-19/"]
URL = st.sidebar.selectbox('Link', links)
st.sidebar.header("Select No. of words you want to display")
words = st.sidebar.selectbox("No. of words", range(10, 1000, 10))
if URL is not None:
    r = requests.get(URL)
    #using the web scraping library that is Beautiful Soup
    soup = BeautifulSoup(r.content, 'html.parser')
    #extracting the data that is in 'div' content of HTML page
    table = soup.find('div', attrs = {'id':'main-content'})
    text = table.text
    #cleaning the data with regular expression library
    cleaned_text = re.sub('\t', "", text)
    cleaned_texts = re.split('\n', cleaned_text)
    cleaned_textss = "".join(cleaned_texts)
    st.write("Word Cloud Plot")
    #using stopwords to remove extra words
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(background_color = "white", max_words =
              words,stopwords = stopwords).generate(cleaned_textss)
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("off")
plt.show()
st.pyplot()

st.image(image01, width=800, caption='Rótulo da Imagem 01') 
    
