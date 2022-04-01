import streamlit as st


def render():
    st.title('streamlit入門')

    st.write('Display Image')

    if st.checkbox("Can you say the same? 'Cause I'm raring to go."):
        audio_file = open('/Users/koutanitta/Desktop/udemy/python/streamlit/おさゆボイス/あーーーーーーう.O.wav', 'rb')
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format='audio/ogg')
