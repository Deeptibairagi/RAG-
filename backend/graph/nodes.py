
from langchain_core.messages import SystemMessage

from langgraph.prebuilt import ToolNode

from backend.graph.state import ChatState

from backend.llm.model import chat_model

from backend.tools.tool_registry import TOOLS


# ==========================================================
# SYSTEM PROMPT
# ==========================================================

SYSTEM_PROMPT = """
You are a helpful AI assistant.

You have access to:

1. DuckDuckGo web search
2. Stock price tool
3. Calculator
4. EMI calculator

Use tools whenever appropriate.

For current information such as:

- weather
- latest news
- recent events
- current information
- current company information

use DuckDuckGo search.

For stock prices use get_stock_price.

For mathematical calculations use calculator.

For loan EMI use calculate_emi.

If the user provides uploaded document content,
answer questions using that document content.

Do not invent information.

If a tool is required:

1. Call the tool.
2. Wait for the result.
3. Use the result.
4. Give a clear final answer.

Do not expose internal tool calls to the user.

When returning calculator or EMI results,
give a human-readable answer instead of returning
a raw Python dictionary.
"""


# ==========================================================
# LLM WITH TOOLS
# ==========================================================

llm_with_tools = chat_model.bind_tools(TOOLS)


# ==========================================================
# CHAT NODE
# ==========================================================

def chat_node(state: ChatState):

    messages = state["messages"]

    system_message = SystemMessage(content=SYSTEM_PROMPT)

    response = llm_with_tools.invoke([system_message] + messages)

    return {"messages": [response]}


# ==========================================================
# TOOL NODE
# ==========================================================

tool_node = ToolNode(TOOLS)


