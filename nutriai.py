import streamlit as st 
st.header("NUTRI AI") 

import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyAd7_7KEVztjv6psnI97b7qkf0JuoGILEc")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")


a=st.text_input("Enter anything you want to know") 
if a:
    st.write(model.generate_content(a).text)
    
