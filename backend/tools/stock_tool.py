
import requests

from langchain_core.tools import tool

from config.settings import ALPHA_VANTAGE_API_KEY


@tool
def get_stock_price(symbol: str) -> dict:

    """
    Get the latest stock price
    using Alpha Vantage.
    """

    if not ALPHA_VANTAGE_API_KEY:

        return {"error":"ALPHA_VANTAGE_API_KEY is not configured."}

    symbol = symbol.upper().strip()

    url = ("https://www.alphavantage.co/query"
        "?function=GLOBAL_QUOTE"
        f"&symbol={symbol}"
        f"&apikey={ALPHA_VANTAGE_API_KEY}"
    )

    try:

        response = requests.get(url, timeout=10)

        response.raise_for_status()

        data = response.json()

        if "Global Quote" not in data:

            return {"error": "Stock information was not available.", "response": data}

        return data

    except requests.RequestException as e:

        return {"error": str(e)}