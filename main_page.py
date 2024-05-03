import streamlit as st
import openai_st
from st_pages import Page, Section, show_pages

st.set_page_config(page_title='St_Stream', page_icon=':robot_face: ')
st.title('AI Language Teacher')
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []


show_pages(
    [
        Page("main_page.py", "Startseite"),
        Section(name="Das Leben am Arbeitsplatz: Bauarbeiten"),
        Page("other_pages/bauarbeiten_vocab.py", "• Vokabeln"),
        Page("other_pages/bauarbeiten_conv.py", "• Gespräch"),
        Section(name="Das Leben am Arbeitsplatz: Büro"),
        Page("other_pages/buro_vocab.py", "• Vokabeln"),
        Page("other_pages/buro_conv.py", "• Gespräch"),
    ]
)

input = st.text_area('Prompt...', key='input')
submit_button = st.button('Submit', type='primary')
box = st.empty()

if submit_button and input:
    st.session_state.chat_history.append(('user', input))
    response = openai_st.stream(
        model='gpt-4-turbo-preview', prompt=input, box=box)
    st.session_state.chat_history.append(('ai', response))

with st.expander("Chat History"):
    for speaker, text in reversed(st.session_state.chat_history):
        if speaker == 'user':
            col1, col2 = st.columns([0.8, 0.2])
            col1.markdown(f"**You:** {text}")
        elif speaker == 'ai':
            col1, col2 = st.columns([0.2, 0.8])
            col2.markdown(f"**AI:** {text}", unsafe_allow_html=True)
