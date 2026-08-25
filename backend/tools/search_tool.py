from langchain_community.tools import DuckDuckGoSearchRun
from ddgs.exceptions import TimeoutException


ddg_search = DuckDuckGoSearchRun()


def safe_web_search(query: str) -> str:
    try:
        result = ddg_search.invoke(query)

        if not result:
            return "No web search results were found."

        return result

    except TimeoutException:
        return (
            "Web search timed out. "
            "Please answer using the available knowledge and retrieved documents."
        )

    except Exception as e:
        return (
            "Web search is temporarily unavailable. "
            "Please answer using the available knowledge and retrieved documents."
        )