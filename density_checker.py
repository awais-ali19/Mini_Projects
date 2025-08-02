import streamlit as st 
import re

st.markdown("<h1 style='text-align: center;'> Density Checker </h1>" , unsafe_allow_html=True)
st.markdown("---")
text = st.text_area("Enter the text")
col1 , col2 , col3 = st.columns(3)
word_dict = dict()
if text:
    col1.markdown("<h3 style='text-align: center;'> Keyword </h3>" , unsafe_allow_html=True)
    col2.markdown("<h3 style='text-align: center;'> Occurences </h3>" , unsafe_allow_html=True)
    col3.markdown("<h3 style='text-align: center;'> Percentage</h3>" , unsafe_allow_html=True)
    simple_text = re.sub("[?.,!*&#;:']" , "" , text)
    words = simple_text.lower().split(" ")
    total_words = len(words)
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    keys = list(word_dict.keys())
    values = list(word_dict.values())
    for i in range(len(keys)):
        col1.markdown(f"<h5 style='text-align: center;'>{keys[i]}</h5>" , unsafe_allow_html=True)
        col2.markdown(f"<h5 style='text-align: center;'>{values[i]}</h5>" , unsafe_allow_html=True)
        col3.markdown(f"<h5 style='text-align: center;'>{(round((values[i]/total_words)*100))}%</h3>" , unsafe_allow_html=True)
        