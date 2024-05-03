import streamlit as st
import openai_st
from prompts import vocab

history = vocab['office']['vocab']
st.set_page_config(page_title='St_Stream', page_icon=':robot_face: ')
st.title('AI Language Teacher')
st.header("Das Büro")
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_area('Prompt...', key='input')
submit_button = st.button('Submit', type='primary')
box = st.empty()

if submit_button and input:
    st.session_state.chat_history.append(('user', input))
    response = openai_st.stream(
        model='gpt-4-turbo-preview', prompt=input, box=box, history=history)
    st.session_state.chat_history.append(('ai', response))

with st.expander("Chat History"):
    for speaker, text in reversed(st.session_state.chat_history):
        if speaker == 'user':
            col1, col2 = st.columns([0.8, 0.2])
            col1.markdown(f"**You:** {text}")
        elif speaker == 'ai':
            col1, col2 = st.columns([0.2, 0.8])
            col2.markdown(f"**AI:** {text}", unsafe_allow_html=True)
