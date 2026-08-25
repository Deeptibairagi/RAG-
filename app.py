

# import streamlit as st

# from config.settings import (
#     APP_TITLE,
#     APP_ICON
# )

# from services.thread_service import (
#     initialize_threads,
#     restore_chat
# )

# from utils.session_state import (
#     initialize_session_state
# )

# from ui.sidebar import (
#     render_sidebar
# )

# from ui.chat import (
#     create_chat_container,
#     render_chat_history
# )

# from ui.chat_input import (
#     render_chat_input
# )


# # ==========================================================
# # PAGE CONFIG
# # ==========================================================

# st.set_page_config(
#     page_title=APP_TITLE,
#     page_icon=APP_ICON,
#     layout="wide"
# )


# # ==========================================================
# # INITIALIZE THREADS
# # ==========================================================

# initialize_threads()

# threads = st.session_state.get(
#     "chat_threads",
#     []
# )


# # ==========================================================
# # INITIALIZE SESSION STATE
# # ==========================================================

# initialize_session_state(
#     threads
# )


# # ==========================================================
# # RESTORE CURRENT CHAT
# # ==========================================================

# if not st.session_state["message_history"]:

#     restore_chat(
#         st.session_state["thread_id"]
#     )


# # ==========================================================
# # SIDEBAR
# # ==========================================================

# render_sidebar()


# # ==========================================================
# # MAIN TITLE
# # ==========================================================

# st.title(
#     "Think Smarter. Work Faster"
# )

# st.markdown(
#     """
#     <div style="font-size: 15px; line-height: 1.2;">
#     👋 <b>Hello! I'm your AI Assistant</b><br>
#     Powered by LangGraph & Large Language Models — here to help you
#     think, search, upload files and calculate smarter.
#     <br><br>
#     💬 <b>Ask anything</b> — General knowledge & explanations<br>
#     🌦️ <b>Live weather</b> — "Weather in Chennai"<br>
#     📈 <b>Stock prices</b> — "Price of HDFC Bank stock"<br>
#     🧮 <b>Calculations</b> — "Calculate EMI for ₹10L at 9% for 5 years"
#     <br><br>
#     <b>How can I assist you today?</b>
#     <br><br>
#     </div>
#     """,
#     unsafe_allow_html=True
# )


# # ==========================================================
# # CHAT CONTAINER
# # ==========================================================

# chat_container = create_chat_container()


# # ==========================================================
# # CHAT HISTORY
# # ==========================================================

# render_chat_history(
#     chat_container
# )


# # ==========================================================
# # CHAT INPUT
# # ==========================================================

# render_chat_input(
#     chat_container
# )



import streamlit as st

from config.settings import (
    APP_TITLE,
    APP_ICON
)

from services.thread_service import (
    initialize_threads,
    restore_chat
)

from utils.session_state import (
    initialize_session_state
)

from ui.sidebar import (
    render_sidebar
)

from ui.chat import (
    create_chat_container,
    render_chat_history
)

from ui.chat_input import (
    render_chat_input
)


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide"
)


# ==========================================================
# INITIALIZE THREADS
# ==========================================================

initialize_threads()

threads = st.session_state.get(
    "chat_threads",
    []
)


# ==========================================================
# INITIALIZE SESSION STATE
# ==========================================================

initialize_session_state(
    threads
)


# ==========================================================
# RESTORE CURRENT CHAT
# ==========================================================

if not st.session_state["message_history"]:

    restore_chat(
        st.session_state["thread_id"]
    )


# ==========================================================
# SIDEBAR
# ==========================================================

render_sidebar()


# ==========================================================
# MAIN TITLE
# ==========================================================

st.title(
    "Think Smarter. Work Faster"
)


# ==========================================================
# INTRODUCTION
# ==========================================================

st.markdown(
    """
    <div style="font-size: 15px; line-height: 1.2;">

    👋 <b>Hello! I'm your AI Assistant</b><br>

    Powered by LangGraph & Large Language Models —
    here to help you think, search, upload files
    and calculate smarter.

    <br><br>

    💬 <b>Ask anything</b> — General knowledge & explanations<br>

    🌦️ <b>Live weather</b> — "Weather in Chennai"<br>

    📈 <b>Stock prices</b> — "Price of HDFC Bank stock"<br>

    🧮 <b>Calculations</b> —
    "Calculate EMI for ₹10L at 9% for 5 years"

    <br><br>

    <b>How can I assist you today?</b>

    </div>
    """,
    unsafe_allow_html=True
)


# ==========================================================
# CHAT CONTAINER
# ==========================================================

chat_container = create_chat_container()


# ==========================================================
# CHAT HISTORY
# ==========================================================

render_chat_history(
    chat_container
)


# ==========================================================
# CHAT INPUT
# ==========================================================

render_chat_input(
    chat_container
)