import os

import streamlit as st 
from dotenv import load_dotenv
import google.generativeai as gen_ai

pwd = os.getcwd()

load_dotenv(pwd + '\\.env')

st.set_page_config(
    page_title='Chat with Gemini-Pro!',
    page_icon=':brain:',  # Favicon Emoji
    layout='centered', 
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')


# To ensure uniformity in terminologies between streamlit and gemini-pro
def translate_role_for_streamlit(user_role):
    if user_role == 'model':
        return 'assistant'
    else:
        return user_role
    
# To initialize chat sesssion in Streamlit if already not present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.title("Cobest Kenya ChatBot")

for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

user_prompt = st.chat_input("Ask AI...")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    gemini_response = st.session_state.chat_session.send_message(user_prompt)
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)

        
