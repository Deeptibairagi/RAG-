import streamlit as st

from langchain_core.messages import HumanMessage

from backend.repositories.thread_repository import load_conversation, retrieve_all_threads, delete_thread

from utils.message_utils import convert_messages_for_ui


# ==========================================================
# INITIAL THREADS
# ==========================================================

def initialize_threads():

    if "chat_threads" not in st.session_state:

        st.session_state["chat_threads"] = retrieve_all_threads()


# ==========================================================
# THREAD TITLE
# ==========================================================

def get_thread_title(thread_id):

    messages = load_conversation(thread_id)

    for message in messages:

        if not isinstance(message, HumanMessage):

            continue

        title = str(message.content).strip()

        if not title:
            continue

        if "USER QUESTION:" in title:

            title = title.split("USER QUESTION:", 1 )[1].strip()

        if len(title) > 40:

            title = (title[:40] + "...")

        return title

    return "New Chat"


# ==========================================================
# RESTORE CHAT
# ==========================================================

def restore_chat(thread_id):

    messages = load_conversation(thread_id)

    st.session_state["message_history"] = convert_messages_for_ui(messages)


# ==========================================================
# LOAD TITLES
# ==========================================================

def initialize_titles():

    if "chat_titles" not in st.session_state:

        st.session_state["chat_titles"] = {}

    for thread_id in st.session_state["chat_threads"]:

        if thread_id not in st.session_state["chat_titles"]:

            st.session_state["chat_titles"][thread_id] = get_thread_title(thread_id)


# ==========================================================
# DELETE THREAD
# ==========================================================

def remove_thread(thread_id):

    success = delete_thread(thread_id)

    if not success:

        return False

    if thread_id in st.session_state["chat_threads"]:

        st.session_state["chat_threads"].remove(thread_id)

    st.session_state["chat_titles"].pop(thread_id, None)

    return True


