from urllib.error import URLError
import streamlit as st
import requests

import numpy as np
import pandas as pd


# Text that goes on the navigator tab

st.set_page_config(
            page_title="Fake News Detector", # => Quick reference - Streamlit
            page_icon="🔎",
            layout="centered", # wide
            initial_sidebar_state="auto") # collapsed


# Content that goes on the sidebar

st.sidebar.markdown("""
    # Some information
    Context of the project, data sources, methodology (algorithms that we've chosen, parameters, evaluation metrics), constraints, etc.

    Some info about the authors
    """)


# IN CASE WE WANT TO SELECT A BACKGROUND PIC

# CSS = """
# h1 {
#     color: red;
# }
# .stApp {
#     background-image: url(https://avatars1.githubusercontent.com/u/9978111?v=4);
#     background-size: cover;
# }
# """
#st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)


# Title, subtitle and text input

st.markdown("<h1 style='text-align: left; color: SteelBlue;'>Fake News Detector</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: left; color: LightSteelBlue; font_size: 40px'><i>The truth will set you free<i></h3>", unsafe_allow_html=True)

""
""

st.markdown("""
## Text input
    """)

txt = st.text_area("Please, insert the article to be analyzed in the box below:","")

st.write('Length:', len(txt))

if st.checkbox('Show progress bar'):
    import time

    'Analyzing text...'

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.01)

    '...and we\'re done!'


fakenews_api_url = URL
response = requests.get(fakenews_api_url, params=txt)

prediction = response.json()

pred = prediction[CLASS]

if pred == 'True':
    st.success(f"""With an accuracy of {accuracy*100}%, our model asserts that what this article says the truth!""")
    # Display funny pic/gif
elif pred == 'Fake':
    st.error(f"""Fake! (funny text)""")
    # Display funny pic/gif
else:
    st.warning("""Hmm... this doesn't sound like a news article""")
    # Display funny pic/gif
