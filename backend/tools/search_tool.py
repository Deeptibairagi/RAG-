from langchain_core.tools import tool
from ddgs import DDGS


@tool
def web_search(query: str) -> str:
    """
    Search the web for current information.
    """

    try:
        with DDGS(timeout=10) as ddgs:
            results = list(
                ddgs.text(
                    query,
                    max_results=5
                )
            )

        if not results:
            return "No web search results found."

        output = []

        for result in results:
            title = result.get("title", "")
            body = result.get("body", "")
            url = result.get("href", "")

            output.append(
                f"Title: {title}\n"
                f"Content: {body}\n"
                f"URL: {url}"
            )

        return "\n\n".join(output)

    except Exception as e:
        print(f"Web search error: {e}")

        return (
            "Web search is currently unavailable. "
            "Please answer using the available knowledge."
        )