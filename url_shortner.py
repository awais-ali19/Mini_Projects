import streamlit as st 
import pyshorteners as pyst
import pyperclip

def copying():
    pyperclip.copy(shorted_url)
s = pyst.Shortener()
st.markdown("<h1 style='text-align: center;'> URL Shortener </h1>" , unsafe_allow_html=True)
form = st.form("name")
url = form.text_input("Enter URL")
s_btn = form.form_submit_button("Short")
if s_btn:
    shorted_url = s.tinyurl.short(url)
    st.markdown("<h3 style='text-align: center;'> Shorted URL </h3>" , unsafe_allow_html=True)
    st.markdown(f"<h6 style='text-align: center;'>{shorted_url}</h6>" , unsafe_allow_html=True)
    st.button("Copy" , on_click=copying())
    