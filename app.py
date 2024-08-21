import streamlit as st
import google.generativeai as genai


st.title("Raja AI")




genai.configure(api_key="AIzaSyCqXw_MgVjtud_ZOiwlmWfjqf-yDktpQNo")
 
text = st.text_input("Enter your question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)
