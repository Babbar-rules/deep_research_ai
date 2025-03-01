from langgraph.graph import StateGraph, START, END
from agents.researcher import research_agent
from agents.synthesizer import synthesis_agent
from utils.state import State

graph_builder = StateGraph(State)

# Add nodes
graph_builder.add_node("researcher", research_agent)
graph_builder.add_node("synthesizer", synthesis_agent)

# Add edges
graph_builder.add_edge(START, "researcher")
graph_builder.add_edge("researcher", "synthesizer")
graph_builder.add_edge("synthesizer", END)
graph= graph_builder.compile()