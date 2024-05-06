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
