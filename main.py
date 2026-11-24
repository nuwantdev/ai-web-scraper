import streamlit as st

st.title("Intelligent Web Scraper")
st.text_input("Enter web URL you want to scrape:")

if st.button("Scrape Site"):
    st.write("Scraping the website")
