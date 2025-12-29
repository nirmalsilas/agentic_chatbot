import streamlit as st
from src.langgraphagentic_ai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagentic_ai.LLMS.groqllm import groqLLM
from src.langgraphagentic_ai.graph.graph_builder import GraphBuilder
from src.langgraphagentic_ai.ui.streamlitui.display_result import DisplayResultStreamlit
def load_langgraph_agenticai_app():

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("error :failed to load user input from UI")
        return 
    user_message = st.chat_input("Enter your message:")

    
    if user_message:

        try:
            llm_object = groqLLM(user_control_inputs = user_input)
            model = llm_object.get_llm_model()
            if not model:
                st.error("Error: not able to initialize the llm")
                return
            print("llm initialized... ",user_message)
            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error("Error: No use case selected")
                return
            
            graph_builder = GraphBuilder(model)

            try:
                graph = graph_builder.setup_graph(usecase)
                print("graph is built... ")
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: graph setup failed {e}")
                return 

        except Exception as e:
            st.error(f"Error: invalid user message {e}")
            return
        




