import streamlit as st

import numpy as np
import pandas as pd

st.set_page_config(
            page_title="Fake News Detector", # => Quick reference - Streamlit
            page_icon="🐍",
            layout="centered", # wide
            initial_sidebar_state="auto") # collapsed

st.sidebar.markdown("""
    # Some information
    Perhaps, context of the project and methodology.

    Some info about the authors
    """)




st.markdown("""

# Fake News Detector Prototype

## _The truth will set you free_

This is text

Whenever I save something it gets displayed
""")

txt = st.text_area('Text to be analyzed', '''

    ''')

st.write('Length:', len(txt))

if st.checkbox('Show progress bar'):
    import time

    'Starting a long computation...'

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

    '...and now we\'re done!'

    st.success('This is a success!')
