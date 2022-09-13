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

st.markdown("<h1 style='text-align: left; color: SteelBlue;'>🔎📰 Fake News Detector 📰🔍</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: left; color: LightSteelBlue; font_size: 40px'><i>The truth will set you free<i></h3>", unsafe_allow_html=True)

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


    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Analyzing text... 🥁🥁🥁 {i+1}')
        bar.progress(i + 1)
        time.sleep(0.02)

    st.markdown("""...and we\'re done! 😎""")

    time.sleep(2)



fakenews_api_url = 'https://fakenews-container-ec4glsrwzq-nw.a.run.app/predict'
response = requests.get(fakenews_api_url, params={'txt':txt})

prediction = response.json()

pred = prediction['Class']

if txt == "":
    pass
elif pred == 'Not News':
    st.warning("""Hmm... it doesn't sound like a news article 🤔""")


elif float(pred) > 0.5:

    st.success(f"""✅ Actually seems legit! ✅""")

    st.markdown("![Alt Text](https://c.tenor.com/J5A9wZzn3ZYAAAAd/robert-redford-jeremiah-johnson.gif)")

    st.markdown(f"""### According to our model, the probability of what's being stated in the article above isn't fake is **{round((float(pred)) * 100, 2)}%**! """)

    st.markdown("<h3 style='text-align: left; color: LightSteelBlue; font_size: 40px'>You're good to share it on your family Whatsapp group 😉</h3>", unsafe_allow_html=True)




elif float(pred) < 0.5:
    time.sleep(2)

    st.error(f"""❌ FAKE ALERT! ❌""")

    st.markdown("![Alt Text](https://media.giphy.com/media/jj2dVdPydkajWiSTMd/giphy.gif)")

    time.sleep(2)

    st.markdown(f"""### According to our model, the probability of what's being stated in the article above is fake is **{round((1 - (float(pred))) * 100, 2)}%**! """)

    st.markdown("<h3 style='text-align: left; color: LightCoral; font_size: 40px'>So you should better not spread these words! 😉</h3>", unsafe_allow_html=True)

""
""

""


if pred != 'Not News':


    if st.checkbox('Developed by'):



        columns = st.columns(4)

        adam = columns[0].image("pics/adam.png", width=130)
        columns[0].markdown("<h5 style='text-align: left; color: SteelBlue;'>Adam Goodes</h5>", unsafe_allow_html=True)
        columns[0].markdown("[Linkedin](https://www.linkedin.com/in/goodes-adam)")

        andre = columns[1].image("pics/andre.png", width=130)
        columns[1].markdown("<h5 style='text-align: left; color: SteelBlue;'>André Marinho</h5>", unsafe_allow_html=True)
        columns[1].markdown("[Linkedin](https://www.linkedin.com/in/agmarinho/)")

        charles = columns[2].image("pics/charles.png", width=130)
        columns[2].markdown("<h5 style='text-align: left; color: SteelBlue;'>Charles Chaverot</h5>", unsafe_allow_html=True)
        columns[2].markdown("[Linkedin](https://www.linkedin.com/in/charleschaverot/)")

        lukas = columns[3].image("pics/lukas.png", width=130)
        columns[3].markdown("<h5 style='text-align: left; color: SteelBlue;'>Lukas Freitas</h5>", unsafe_allow_html=True)
        columns[3].markdown("[Linkedin](https://www.linkedin.com/in/maurylukas/)")

        ''

        st.markdown("#### [GitHub Repo](https://github.com/goodesad/fake-news)")
