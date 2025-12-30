import streamlit as st
import os

from src.langgraphagentic_ai.ui.uiconfigfile import Config
class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_control={}
    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_page_title(), layout="wide")
        st.header(self.config.get_page_title())
    
        with st.sidebar:
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            self.user_control["selected_llm"] = st.selectbox("selectLLM", llm_options)
            if self.user_control["selected_llm"] == 'Groq':
                model_options = self.config.get_groq_model_options()
                self.user_control["selected_groq_model"] = st.selectbox("select GROQ Model", model_options)
                self.user_control["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] =st.text_input("API key",type="password")

                if not self.user_control["GROQ_API_KEY"]:
                    st.warning(" please enter your GROQ_API Key")
            self.user_control["selected_usecase"] = st.selectbox("select usecase", usecase_options)
            if self.user_control["selected_usecase"] == "Chatbot with websearch" :
                
                os.environ["TAVILY_API_KEY"] = self.user_control["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] =st.text_input("tavily API key",type="password")
                
                if not self.user_control["TAVILY_API_KEY"]:
                    st.error("Error: please enter the tavily api key ")

        return self.user_control
