
from langgraph.graph import StateGraph, START, END

from backend.graph.state import ChatState

from backend.graph.nodes import chat_node, tool_node

from backend.graph.edges import route_after_chat

from backend.database.checkpoint import checkpointer


# ==========================================================
# CREATE GRAPH
# ==========================================================

graph = StateGraph(ChatState)


# ==========================================================
# NODES
# ==========================================================

graph.add_node("chat_node", chat_node)

graph.add_node("tools", tool_node)


# ==========================================================
# EDGES
# ==========================================================

graph.add_edge(START, "chat_node")

graph.add_conditional_edges("chat_node", route_after_chat)

graph.add_edge("tools", "chat_node")

graph.add_edge("chat_node", END)

# ==========================================================
# COMPILE
# ==========================================================

chatbot = graph.compile(checkpointer=checkpointer)

