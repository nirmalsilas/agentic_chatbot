import streamlit as st
from src.langgraphagentic_ai.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraph_agenticai_app():

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("error :failed to load user input from UI")
        return 
    user_message = st.chat_input("Enter your message:")