from langgraph.graph import StateGraph, START, END
from src.langgraphagentic_ai.state.state import State
from src.langgraphagentic_ai.nodes.basic_chat_node import BasicChatBotNode
from src.langgraphagentic_ai.tools.tools_node import get_tools,create_toolNode
from langgraph.prebuilt import tools_condition,ToolNode
from src.langgraphagentic_ai.nodes.chatbot_tool_node  import ChatbotwithTool



class GraphBuilder:
    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(State)
    
    def basic_chat_build_graph(self):


        self.basicChatbot_node = BasicChatBotNode(self.llm)

        self.graph_builder.add_node("chatbot",self.basicChatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)
    
    def chatbot_with_websearch_build_graph(self):
        tools = get_tools()
        tool_node = create_toolNode(tools)
        llm = self.llm
        
        obj_chatbot_with_tool = ChatbotwithTool(llm)
        chatbot_node = obj_chatbot_with_tool.create_chatbot(tools=tools)


        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools",tool_node)

        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")
        #self.graph_builder.add_edge("chatbot",END)
        
        

    def setup_graph(self,usecase:str):
        if usecase == "Basic chatbot":
            self.basic_chat_build_graph()
            return self.graph_builder.compile()
        if usecase == "Chatbot with websearch":
            self.chatbot_with_websearch_build_graph()
            return self.graph_builder.compile()
                




