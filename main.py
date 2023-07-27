import streamlit as st
import pyshorteners

st.set_page_config(page_title="URL Shortener", page_icon=":link:")

with st.container():
    urlTitleText = st.title("URL Shortener!")
    linkInput = st.text_input("Input link here")
    shortenButton = st.button("Shorten!")

    if shortenButton:
        if len(linkInput) > 0:
            try:
                s = pyshorteners.Shortener()
                st.success(s.tinyurl.short(linkInput))
            except:
                st.error("Please enter a valid link")
        else:
            st.error("Field cannot be left blank")
