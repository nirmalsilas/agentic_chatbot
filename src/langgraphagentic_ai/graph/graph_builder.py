from langgraph.graph import StateGraph, START, END
from src.langgraphagentic_ai.state.state import State
from src.langgraphagentic_ai.nodes.basic_chat_node import BasicChatBotNode





class GraphBuilder:
    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(State)
    
    def basic_chat_build_graph(self):


        self.basicChatbot_node = BasicChatBotNode(self.llm)

        self.GraphBuilder.add_node("chatbot",self.basicChatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def setup_graph(self,usecase:str):
        if usecase == "Basic Chatbot":
                self.basic_chat_build_graph()
                




