

import streamlit as st

from services.thread_service import initialize_titles, restore_chat, remove_thread

from utils.session_state import reset_chat


# ==========================================================
# SIDEBAR
# ==========================================================

def render_sidebar():

    # ======================================================
    # SIDEBAR CSS
    # ======================================================

    st.sidebar.markdown(
        """
        <style>

        /* ==================================================
           REMOVE TOP WHITE SPACE
           ================================================== */

        section[data-testid="stSidebar"] > div {
            padding-top: 0rem !important;
        }

        section[data-testid="stSidebar"]
        div[data-testid="stSidebarContent"] {
            padding-top: 0rem !important;
        }


        /* ==================================================
           PREVENT WHOLE SIDEBAR FROM SCROLLING
           ================================================== */

        section[data-testid="stSidebar"] {
            overflow: hidden !important;
        }

        section[data-testid="stSidebar"] > div {
            overflow: hidden !important;
        }


        /* ==================================================
           CENTER TITLE
           ================================================== */

        .personal-chatbot-title {
            text-align: center;
            font-size: 1.45rem;
            font-weight: 700;

            margin-top: 0px;
            margin-bottom: 0px;

            padding-top: 0px;
            padding-bottom: 0px;
        }

        </style>
        """, unsafe_allow_html=True
    )


    # ======================================================
    # PERSONAL CHATBOT TITLE
    # ======================================================

    st.sidebar.markdown(
        """
        <div class="personal-chatbot-title">
            🤖 Personal Chatbot
        </div>
        """, unsafe_allow_html=True
    )


    # ======================================================
    # INITIALIZE TITLES
    # ======================================================

    initialize_titles()


    # ======================================================
    # ONE ROW GAP
    # ======================================================

    st.sidebar.markdown(
        """
        <div style="height: 12px;"></div>
        """,
        unsafe_allow_html=True
    )


    # ======================================================
    # NEW CHAT
    # ======================================================

    if st.sidebar.button( "➕ New Chat", use_container_width=True, key="new_chat_button"):

        reset_chat()

        st.rerun()


    # ======================================================
    # DIVIDER
    # ======================================================

    st.sidebar.divider()


    # ======================================================
    # RECENT CHATS
    # ======================================================

    st.sidebar.subheader("Recent Chats")


    # ======================================================
    # SCROLLABLE THREAD CONTAINER
    # ======================================================

    thread_container = st.sidebar.container(height=500, border=False)


    # ======================================================
    # THREAD LIST
    # ======================================================

    with thread_container:

        threads = st.session_state.get("chat_threads", [])


        # --------------------------------------------------
        # NO CHATS
        # --------------------------------------------------

        if not threads:

            st.caption("No recent chats")


        # --------------------------------------------------
        # CHAT THREADS
        # --------------------------------------------------

        for thread_id in reversed(threads):

            thread_id = str(thread_id)


            # ==============================================
            # GET TITLE
            # ==============================================

            title = (st.session_state["chat_titles"].get(thread_id, "New Chat"))


            # ==============================================
            # THREAD ROW
            # ==============================================

            col1, col2 = st.columns([5, 1], vertical_alignment="center")


            # ==============================================
            # OPEN CHAT BUTTON
            # ==============================================

            with col1:

                if st.button(title, key=f"open_{thread_id}", use_container_width=True):

                    # Set current thread
                    st.session_state["thread_id"] = thread_id


                    # Restore messages
                    restore_chat(thread_id)


                    # Refresh UI
                    st.rerun()


            # ==============================================
            # DELETE BUTTON
            # ==============================================

            with col2:

                if st.button("🗑️", key=f"delete_{thread_id}", use_container_width=True):

                    success = remove_thread(thread_id)


                    # --------------------------------------
                    # Delete successful
                    # --------------------------------------

                    if success:

                        current_thread = str(st.session_state["thread_id"])


                        # ------------------------------
                        # If deleting current chat
                        # ------------------------------

                        if current_thread == thread_id:

                            reset_chat()


                        # ------------------------------
                        # Refresh
                        # ------------------------------

                        st.rerun()



