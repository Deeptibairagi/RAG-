from backend.database.connection import get_connection

from backend.graph.graph import chatbot


# ==========================================================
# LOAD CONVERSATION
# ==========================================================

def load_conversation(thread_id):

    try:

        config = {"configurable": {"thread_id":str(thread_id)}}

        state = chatbot.get_state(config=config)

        if not state:

            return []

        return state.values.get("messages", [])

    except Exception as e:

        print(
            f"Error loading conversation: {e}"
        )

        return []


# ==========================================================
# GET ALL THREADS
# ==========================================================

def retrieve_all_threads():

    all_threads = set()

    try:

        # Use the same database/checkpointer
        from backend.database.checkpoint import checkpointer

        for checkpoint in checkpointer.list(None):

            config = checkpoint.config

            if "configurable" not in config:
                continue

            thread_id = (config["configurable"].get("thread_id"))

            if thread_id:

                all_threads.add(str(thread_id))

    except Exception as e:

        print(f"Error retrieving threads: {e}")

    return list(all_threads)


# ==========================================================
# DELETE THREAD
# ==========================================================

def delete_thread(thread_id):

    thread_id = str(thread_id)

    conn = None

    try:

        conn = get_connection()

        cursor = conn.cursor()

        tables = cursor.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type='table'
            """
        ).fetchall()

        table_names = {table[0] for table in tables}

        tables_to_clean = [
            "checkpoints",
            "checkpoint_blobs",
            "checkpoint_writes",
            "writes"
        ]

        for table_name in tables_to_clean:

            if table_name in table_names:

                cursor.execute(f""" DELETE FROM {table_name} WHERE thread_id = ? """, (thread_id,))

        conn.commit()

        return True

    except Exception as e:

        print(f"Error deleting thread " f"{thread_id}: {e}")

        return False

    finally:

        if conn:

            conn.close()