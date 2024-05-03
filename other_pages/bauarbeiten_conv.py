import streamlit as st
import openai_st
from speech_to_text import whisper_stt
from prompts import vocab
from utils import tts
history = vocab['construction']['conv']


st.set_page_config(page_title='St_Stream', page_icon=':robot_face: ')
st.title('Das Leben am Arbeitsplatz')
st.header("Die Bauarbeiten")
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []


# input = st.text_area('Prompt...', key='input')

box = st.empty()


text = whisper_stt(language='de')
if text:
    st.write(text)
    st.session_state.chat_history.append(('user', text))
    response = openai_st.stream(
        model='gpt-4-turbo-preview', prompt=text, box=box, history=history)
    st.session_state.chat_history.append(('ai', response))
    filename = tts(response)

    if filename:
        st.audio(filename)

with st.expander("Chat History"):
    for speaker, text in reversed(st.session_state.chat_history):
        if speaker == 'user':
            col1, col2 = st.columns([0.8, 0.2])
            col1.markdown(f"**You:** {text}")
        elif speaker == 'ai':
            col1, col2 = st.columns([0.2, 0.8])
            col2.markdown(f"**AI:** {text}", unsafe_allow_html=True)
