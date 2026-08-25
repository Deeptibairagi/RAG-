

import streamlit as st

from ui.attachments import render_attachment_menu

from ui.chat import render_user_message, render_assistant_stream

from services.chat_service import stream_chat

from utils.session_state import clear_attachment


# ==========================================================
# CREATE THREAD TITLE
# ==========================================================

def create_thread_title(thread_id, user_input):

    current_title = (st.session_state["chat_titles"].get(thread_id, "New Chat"))

    if current_title == "New Chat":

        title = user_input.strip()

        if len(title) > 40:

            title = (title[:40] + "...")

        if not title:

            title = "New Chat"

        st.session_state["chat_titles"][thread_id] = title


# ==========================================================
# HANDLE MESSAGE
# ==========================================================

def handle_message(user_input, chat_container):

    """
    Process a user message and stream the assistant response.

    IMPORTANT:
    Both user and assistant messages are written into the
    SAME autoscrolling chat container.
    """

    thread_id = str(st.session_state["thread_id"])

    uploaded_context = (st.session_state["uploaded_context"])


    # ======================================================
    # CREATE TITLE
    # ======================================================

    create_thread_title(thread_id, user_input)


    # ======================================================
    # USER DISPLAY MESSAGE
    # ======================================================

    display_message = user_input

    if uploaded_context:

        display_message = ("📎 **Document attached**\n\n" + user_input)


    # ======================================================
    # SAVE USER MESSAGE TO SESSION STATE
    # ======================================================

    st.session_state["message_history"].append({"role": "user", "content": display_message})


    # ======================================================
    # RENDER USER MESSAGE
    # ======================================================

    render_user_message(chat_container, display_message)


    # ======================================================
    # CREATE STREAM
    # ======================================================

    response_stream = stream_chat(user_input=user_input, thread_id=thread_id, uploaded_context=uploaded_context)


    # ======================================================
    # STREAM ASSISTANT RESPONSE
    #
    # This is rendered INSIDE chat_container.
    #
    # chat_container has autoscroll=True.
    # ======================================================


    with st.spinner("🤔 AI is thinking..."):
        ai_response = render_assistant_stream(chat_container, response_stream)


    # ======================================================
    # SAVE COMPLETE AI RESPONSE
    # ======================================================

    st.session_state["message_history"].append({"role": "assistant", "content": str(ai_response)})


    # ======================================================
    # CLEAR ATTACHMENT
    # ======================================================

    clear_attachment()


    # ======================================================
    # RERUN
    #
    # On the next run:
    #
    # message_history contains both user + assistant
    # messages, so they are restored normally.
    # ======================================================

    st.rerun()


# ==========================================================
# CHAT INPUT
# ==========================================================

def render_chat_input(chat_container):

    """
    Render the attachment button and chat input at the
    bottom of the application.

    st.bottom keeps this area pinned to the bottom.
    """

    with st.bottom:

        # --------------------------------------------------
        # ATTACHMENT STATUS
        # --------------------------------------------------

        if st.session_state["uploaded_context"]:

            st.caption("📎 Attached: " f"**{st.session_state['uploaded_file_name']}** ""— Ask your question below.")


        # --------------------------------------------------
        # INPUT ROW
        # --------------------------------------------------

        col1, col2 = st.columns([0.8, 9.2], vertical_alignment="bottom")


        # --------------------------------------------------
        # ATTACHMENT BUTTON
        # --------------------------------------------------

        with col1:

            render_attachment_menu()


        # --------------------------------------------------
        # CHAT INPUT
        # --------------------------------------------------

        with col2:

            user_input = st.chat_input("Type your message here ", key="chat_input", submit_mode="disable")


    # ======================================================
    # PROCESS MESSAGE
    #
    # IMPORTANT:
    # This happens AFTER the bottom input has been created.
    #
    # Therefore the bottom input stays in its own fixed
    # bottom area while the response streams into the
    # autoscrolling chat container above it.
    # ======================================================

    if user_input:

        handle_message(user_input, chat_container)