


# import streamlit as st

# from langchain_core.messages import HumanMessage

# from backend.repositories.thread_repository import (
#     load_conversation,
#     retrieve_all_threads,
#     delete_thread
# )

# from utils.message_utils import convert_messages_for_ui


# # ==========================================================
# # INITIAL THREADS
# # ==========================================================

# def initialize_threads():

#     if "chat_threads" not in st.session_state:

#         st.session_state["chat_threads"] = (
#             retrieve_all_threads()
#         )


# # ==========================================================
# # THREAD TITLE
# # ==========================================================

# def get_thread_title(thread_id):

#     messages = load_conversation(thread_id)

#     for message in messages:

#         if not isinstance(message, HumanMessage):
#             continue

#         title = str(
#             message.content
#         ).strip()

#         if not title:
#             continue

#         if "USER QUESTION:" in title:

#             title = title.split(
#                 "USER QUESTION:",
#                 1
#             )[1].strip()

#         if len(title) > 40:

#             title = (
#                 title[:40]
#                 + "..."
#             )

#         return title

#     return "New Chat"


# # ==========================================================
# # RESTORE CHAT
# # ==========================================================

# def restore_chat(thread_id):

#     messages = load_conversation(thread_id)

#     st.session_state["message_history"] = (
#         convert_messages_for_ui(messages)
#     )


# # ==========================================================
# # LOAD TITLES
# # ==========================================================

# def initialize_titles():

#     if "chat_titles" not in st.session_state:

#         st.session_state["chat_titles"] = {}

#     for thread_id in st.session_state.get(
#         "chat_threads",
#         []
#     ):

#         thread_id = str(thread_id)

#         if thread_id not in st.session_state["chat_titles"]:

#             st.session_state["chat_titles"][thread_id] = (
#                 get_thread_title(thread_id)
#             )


# # ==========================================================
# # DELETE THREAD
# # ==========================================================

# def remove_thread(thread_id):

#     thread_id = str(thread_id)

#     # Delete from database
#     success = delete_thread(thread_id)

#     if not success:
#         return False

#     # Remove from session thread list
#     threads = st.session_state.get(
#         "chat_threads",
#         []
#     )

#     st.session_state["chat_threads"] = [
#         str(t)
#         for t in threads
#         if str(t) != thread_id
#     ]

#     # Remove title
#     titles = st.session_state.get(
#         "chat_titles",
#         {}
#     )

#     titles.pop(thread_id, None)

#     st.session_state["chat_titles"] = titles

#     # If deleted thread was active
#     current_thread = str(
#         st.session_state.get(
#             "thread_id",
#             ""
#         )
#     )

#     if current_thread == thread_id:

#         st.session_state["message_history"] = []

#     return True





import streamlit as st

from langchain_core.messages import HumanMessage

from backend.repositories.thread_repository import (
    load_conversation,
    retrieve_all_threads,
    delete_thread
)

from utils.message_utils import convert_messages_for_ui


# ==========================================================
# INITIALIZE THREADS
# ==========================================================

def initialize_threads():
    """
    Load thread IDs from the database only once
    per Streamlit session.
    """

    if "chat_threads" not in st.session_state:

        st.session_state["chat_threads"] = (
            retrieve_all_threads()
        )


# ==========================================================
# GET THREAD TITLE
# ==========================================================

def get_thread_title(thread_id):
    """
    Get the first user message and use it as the
    chat title.
    """

    messages = load_conversation(thread_id)

    for message in messages:

        if not isinstance(message, HumanMessage):
            continue

        title = str(
            message.content
        ).strip()

        if not title:
            continue

        # --------------------------------------------------
        # Remove uploaded-document prefix if present
        # --------------------------------------------------

        if "USER QUESTION:" in title:

            title = title.split(
                "USER QUESTION:",
                1
            )[1].strip()

        # --------------------------------------------------
        # Limit title length
        # --------------------------------------------------

        if len(title) > 40:

            title = (
                title[:40]
                + "..."
            )

        return title

    return "New Chat"


# ==========================================================
# RESTORE CHAT
# ==========================================================

def restore_chat(thread_id):
    """
    Restore messages for the selected thread into
    Streamlit session state.
    """

    messages = load_conversation(thread_id)

    st.session_state["message_history"] = (
        convert_messages_for_ui(messages)
    )


# ==========================================================
# INITIALIZE TITLES
# ==========================================================

def initialize_titles():
    """
    Load titles for all existing threads.
    """

    if "chat_titles" not in st.session_state:

        st.session_state["chat_titles"] = {}

    for thread_id in st.session_state.get(
        "chat_threads",
        []
    ):

        thread_id = str(thread_id)

        if thread_id not in st.session_state["chat_titles"]:

            st.session_state["chat_titles"][thread_id] = (
                get_thread_title(thread_id)
            )


# ==========================================================
# DELETE THREAD
# ==========================================================

def remove_thread(thread_id):
    """
    Delete a thread from:

    1. SQLite / LangGraph database
    2. Streamlit session state
    3. Chat title cache
    4. Current message history if required
    """

    thread_id = str(thread_id)

    # ======================================================
    # DATABASE DELETE
    # ======================================================

    success = delete_thread(thread_id)

    if not success:
        return False

    # ======================================================
    # REMOVE FROM SESSION THREAD LIST
    # ======================================================

    threads = st.session_state.get(
        "chat_threads",
        []
    )

    st.session_state["chat_threads"] = [
        str(thread)
        for thread in threads
        if str(thread) != thread_id
    ]

    # ======================================================
    # REMOVE TITLE
    # ======================================================

    titles = st.session_state.get(
        "chat_titles",
        {}
    )

    titles.pop(
        thread_id,
        None
    )

    st.session_state["chat_titles"] = titles

    # ======================================================
    # CHECK CURRENT THREAD
    # ======================================================

    current_thread = str(
        st.session_state.get(
            "thread_id",
            ""
        )
    )

    # ======================================================
    # IF CURRENT THREAD WAS DELETED
    # ======================================================

    if current_thread == thread_id:

        st.session_state["message_history"] = []

    return True