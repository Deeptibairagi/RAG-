
# from backend.database.connection import get_connection
# from backend.graph.graph import chatbot


# # ==========================================================
# # LOAD CONVERSATION
# # ==========================================================

# def load_conversation(thread_id):

#     try:

#         config = {
#             "configurable": {
#                 "thread_id": str(thread_id)
#             }
#         }

#         state = chatbot.get_state(config=config)

#         if not state:
#             return []

#         return state.values.get("messages", [])

#     except Exception as e:

#         print(f"Error loading conversation: {e}")

#         return []


# # ==========================================================
# # GET ALL THREADS
# # ==========================================================

# def retrieve_all_threads():

#     all_threads = set()

#     try:

#         from backend.database.checkpoint import checkpointer

#         for checkpoint in checkpointer.list(None):

#             config = checkpoint.config

#             if not config:
#                 continue

#             configurable = config.get("configurable", {})

#             thread_id = configurable.get("thread_id")

#             if thread_id:

#                 all_threads.add(str(thread_id))

#     except Exception as e:

#         print(f"Error retrieving threads: {e}")

#     return list(all_threads)


# # ==========================================================
# # DELETE THREAD
# # ==========================================================

# def delete_thread(thread_id):

#     thread_id = str(thread_id)

#     conn = None

#     try:

#         conn = get_connection()

#         cursor = conn.cursor()

#         # Get all tables
#         tables = cursor.execute(
#             """
#             SELECT name
#             FROM sqlite_master
#             WHERE type = 'table'
#             """
#         ).fetchall()

#         table_names = {
#             str(table[0])
#             for table in tables
#         }

#         # LangGraph SQLite tables
#         tables_to_clean = [
#             "checkpoints",
#             "checkpoint_blobs",
#             "checkpoint_writes",
#             "writes"
#         ]

#         deleted = False

#         for table_name in tables_to_clean:

#             if table_name not in table_names:
#                 continue

#             # Check whether thread_id exists
#             columns = cursor.execute(
#                 f"PRAGMA table_info({table_name})"
#             ).fetchall()

#             column_names = {
#                 column[1]
#                 for column in columns
#             }

#             if "thread_id" not in column_names:
#                 continue

#             cursor.execute(
#                 f"""
#                 DELETE FROM {table_name}
#                 WHERE thread_id = ?
#                 """,
#                 (thread_id,)
#             )

#             if cursor.rowcount > 0:
#                 deleted = True

#         conn.commit()

#         print(
#             f"Deleted thread {thread_id}: {deleted}"
#         )

#         return True

#     except Exception as e:

#         print(
#             f"Error deleting thread {thread_id}: {e}"
#         )

#         if conn:
#             conn.rollback()

#         return False

#     finally:

#         if conn:
#             conn.close()




from backend.graph.graph import chatbot
from backend.database.checkpoint import checkpointer


# ==========================================================
# LOAD CONVERSATION
# ==========================================================

def load_conversation(thread_id):
    """
    Load all messages for a conversation thread.
    """

    thread_id = str(thread_id)

    try:
        config = {
            "configurable": {
                "thread_id": thread_id
            }
        }

        state = chatbot.get_state(config=config)

        if not state:
            return []

        return state.values.get("messages", [])

    except Exception as e:
        print(
            f"Error loading conversation {thread_id}: {e}"
        )

        return []


# ==========================================================
# GET ALL THREADS
# ==========================================================

def retrieve_all_threads():
    """
    Retrieve all thread IDs stored by LangGraph.
    """

    all_threads = set()

    try:
        for checkpoint in checkpointer.list(None):

            config = checkpoint.config

            if not config:
                continue

            configurable = config.get(
                "configurable",
                {}
            )

            thread_id = configurable.get(
                "thread_id"
            )

            if thread_id:
                all_threads.add(
                    str(thread_id)
                )

    except Exception as e:

        print(
            f"Error retrieving threads: {e}"
        )

    return list(all_threads)


# ==========================================================
# DELETE THREAD
# ==========================================================

def delete_thread(thread_id):
    """
    Delete a complete LangGraph conversation.

    Uses LangGraph's official delete_thread()
    instead of manually deleting SQLite tables.
    """

    thread_id = str(thread_id)

    try:

        # --------------------------------------------------
        # DELETE FROM LANGGRAPH CHECKPOINTER
        # --------------------------------------------------

        checkpointer.delete_thread(
            thread_id
        )

        print(
            f"Successfully deleted thread: {thread_id}"
        )

        return True

    except Exception as e:

        print(
            f"Error deleting thread {thread_id}: {e}"
        )

        return False