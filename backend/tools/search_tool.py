from langchain_community.tools import DuckDuckGoSearchRun

from langchain_core.tools import tool

search_tool = DuckDuckGoSearchRun()




def web_search(query: str) -> str:
    """
    Search the web using DuckDuckGo.
    """

    if not query or not query.strip():
        return "Please provide a search query."

    try:
        result = search_tool.invoke(query)

        return str(result)

    except Exception as e:
        return f"Search failed: {str(e)}"