

import uuid
import streamlit as st


# ==========================================================
# THREAD ID
# ==========================================================

def generate_thread_id():

    return str(uuid.uuid4())


# ==========================================================
# ADD THREAD
# ==========================================================

def add_thread(thread_id):

    thread_id = str(thread_id)

    if (thread_id not in st.session_state["chat_threads"]):

        st.session_state["chat_threads"].append(thread_id)


# ==========================================================
# INITIALIZE SESSION STATE
# ==========================================================

def initialize_session_state(threads):

    # ------------------------------------------------------
    # THREADS
    # ------------------------------------------------------

    if "chat_threads" not in st.session_state:

        st.session_state["chat_threads"] = list(threads)


    # ------------------------------------------------------
    # CURRENT THREAD
    # ------------------------------------------------------

    if "thread_id" not in st.session_state:

        st.session_state["thread_id"] = generate_thread_id()


    # ------------------------------------------------------
    # TITLES
    # ------------------------------------------------------

    if "chat_titles" not in st.session_state:

        st.session_state["chat_titles"] = {}


    # ------------------------------------------------------
    # MESSAGE HISTORY
    # ------------------------------------------------------

    if "message_history" not in st.session_state:

        st.session_state["message_history"] = []


    # ------------------------------------------------------
    # UPLOADED CONTEXT
    # ------------------------------------------------------

    if "uploaded_context" not in st.session_state:

        st.session_state["uploaded_context"] = ""


    # ------------------------------------------------------
    # UPLOADED FILE NAME
    # ------------------------------------------------------

    if "uploaded_file_name" not in st.session_state:

        st.session_state["uploaded_file_name"] = ""


    # ------------------------------------------------------
    # UPLOADED SOURCE
    # ------------------------------------------------------

    if "uploaded_source" not in st.session_state:

        st.session_state["uploaded_source"] = ""


    # ------------------------------------------------------
    # ADD CURRENT THREAD
    # ------------------------------------------------------

    add_thread(st.session_state["thread_id"])


# ==========================================================
# CLEAR ATTACHMENT
# ==========================================================

def clear_attachment():

    st.session_state["uploaded_context"] = ""

    st.session_state["uploaded_file_name"] = ""

    st.session_state["uploaded_source"] = ""


# ==========================================================
# RESET CHAT
# ==========================================================

def reset_chat():

    thread_id = generate_thread_id()


    # ------------------------------------------------------
    # CURRENT THREAD
    # ------------------------------------------------------

    st.session_state["thread_id"] = thread_id


    # ------------------------------------------------------
    # ADD THREAD
    # ------------------------------------------------------

    add_thread(thread_id)


    # ------------------------------------------------------
    # TITLE
    # ------------------------------------------------------

    st.session_state["chat_titles"][thread_id] = "New Chat"


    # ------------------------------------------------------
    # CLEAR MESSAGES
    # ------------------------------------------------------

    st.session_state["message_history"] = []


    # ------------------------------------------------------
    # CLEAR ATTACHMENT
    # ------------------------------------------------------

    clear_attachment()





