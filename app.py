from urllib.error import URLError
import streamlit as st
import requests
import time
import webbrowser


# Text that goes on the navigator tab

st.set_page_config(
            page_title="Fake News Detector", # => Quick reference - Streamlit
            page_icon="🔎",
            layout="centered", # wide
            initial_sidebar_state="auto") # collapsed



# IN CASE WE WANT TO SELECT A BACKGROUND PIC

# CSS = """
# h1 {
#     color: red;
# }
# .stApp {
#     background-image: url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5IPGVzeiI06TDGsUrHEEoBpRV--xJhCKXRGiqY6u4P6JKkPTHzoduSur1d2L3VrEScmE&usqp=CAU);
#     background-size: cover;
# }
# """
# st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)


st.markdown("<h1 style='text-align: left; color: LightSteelBlue;'>Fake News Detector</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: left; color: AntiqueWhite; font_size: 40px'><i>The truth will set you free<i></h3>", unsafe_allow_html=True)

""
""

st.markdown("""
## Text input
    """)

txt = st.text_area("Please, insert the article to be analyzed in the box below:","")

st.write('Length:', len(txt))

# if st.checkbox('Show progress bar'):
#     import time

#     'Analyzing text...'

#     # Add a placeholder
#     latest_iteration = st.empty()
#     bar = st.progress(0)

#     for i in range(100):
#         # Update the progress bar with each iteration.
#         latest_iteration.text(f'Iteration {i+1}')
#         bar.progress(i + 1)
#         time.sleep(0.01)

#     '...and we\'re done!'





# Add a placeholder

if txt != "":

    'Analyzing text...'
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.02)

    '...and we\'re done!'


fakenews_api_url = 'https://fakenews-container-ec4glsrwzq-nw.a.run.app/predict'
response = requests.get(fakenews_api_url, params={'txt':txt})

prediction = response.json()

pred = prediction['Class']

if txt == "":
    pass
elif pred == 'Not News':
    st.warning("""Hmm... this doesn't sound like a news article""")
    # Display funny pic/gif

elif float(pred) > 0.5:
    st.success(f"""Message displayed for success (True)!

    Pred value:{pred}""")
    # Display funny pic/gif
elif float(pred) < 0.5:
    st.error(f"""Message displayed for fake.

    Pred value:{pred}""")
    # Display funny pic/gif

""
""
""
""
""
""


if pred != False:

    time.sleep(5)

    st.markdown("""
        ## Developed by
            """)

    ""

    columns = st.columns(4)

    adam = columns[0].image("pics/adam.png", width=140)
    columns[0].markdown("<h4 style='text-align: left; color: white;'>Adam Goodes</h4>", unsafe_allow_html=True)
    columns[0].markdown("[Linkedin](https://www.linkedin.com/)")

    andre = columns[1].image("pics/andre.png", width=140)
    columns[1].markdown("<h4 style='text-align: left; color: white;'>André Marinho</h4>", unsafe_allow_html=True)
    columns[1].markdown("[Linkedin](https://www.linkedin.com/in/agmarinho/)")

    charles = columns[2].image("pics/charles.png", width=140)
    columns[2].markdown("<h4 style='text-align: left; color: white;'>Charles Chaverot</h4>", unsafe_allow_html=True)
    columns[2].markdown("[Linkedin](https://www.linkedin.com/)")

    lukas = columns[3].image("pics/lukas.png", width=140)
    columns[3].markdown("<h4 style='text-align: left; color: white;'>Lukas Freitas</h4>", unsafe_allow_html=True)
    columns[3].markdown("[Linkedin](https://www.linkedin.com/)")

    ""

    if st.checkbox('Further details on the project'):
        st.markdown("""
        # Some information

        Optional: Context of the project, data sources, methodology (algorithms that we've chosen, parameters, evaluation metrics), constraints, etc.

        Some info about the authors
        """)
