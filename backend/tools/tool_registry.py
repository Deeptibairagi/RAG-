from backend.tools.search_tool import web_search

from backend.tools.emi_tool import calculate_emi

from backend.tools.stock_tool import get_stock_price


# ==========================================================
# ALL TOOLS
# ==========================================================

TOOLS = [web_search, get_stock_price, calculate_emi]