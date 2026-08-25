

import streamlit as st


# ==========================================================
# CREATE CHAT CONTAINER
# ==========================================================

def create_chat_container():

    """
    Creates the main chat area.

    autoscroll=True is important because it automatically
    keeps the bottom/latest content visible while streaming.
    """

    return st.container(autoscroll=True)


# ==========================================================
# CHAT HISTORY
# ==========================================================

def render_chat_history(chat_container):

    """
    Render all previously saved messages inside the
    autoscrolling chat container.
    """

    with chat_container:

        for message in st.session_state["message_history"]:

            role = message.get("role", "assistant")

            content = message.get("content", "")

            if not content:
                continue

            with st.chat_message(role):

                st.markdown(content)


# ==========================================================
# USER MESSAGE
# ==========================================================

def render_user_message(chat_container, content):

    """
    Render the user's latest message inside the same
    autoscrolling chat container.
    """

    with chat_container:

        with st.chat_message("user"):

            st.markdown(content)


# ==========================================================
# ASSISTANT STREAM
# ==========================================================

def render_assistant_stream(chat_container, response_stream):

    """
    Render the streaming assistant response inside the
    autoscrolling chat container.

    st.write_stream() updates the content as chunks arrive.
    Because the parent container has autoscroll=True,
    the latest tokens remain visible.
    """

    with chat_container:

        with st.chat_message("assistant"):

            return st.write_stream(response_stream)