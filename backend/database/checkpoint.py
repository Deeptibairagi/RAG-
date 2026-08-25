

from langgraph.checkpoint.sqlite import SqliteSaver

from backend.database.connection import get_connection


# ==========================================================
# DATABASE CONNECTION
# ==========================================================

conn = get_connection()


# ==========================================================
# CHECKPOINTER
# ==========================================================

checkpointer = SqliteSaver(conn=conn)