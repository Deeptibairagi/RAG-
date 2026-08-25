

from langchain_core.messages import HumanMessage, AIMessage

from backend.graph.graph import chatbot


# ==========================================================
# BUILD ACTUAL MESSAGE
# ==========================================================

def build_actual_message(user_input, uploaded_context):

    if uploaded_context:

        return (uploaded_context + "\n\nUSER QUESTION:\n" + user_input)

    return user_input


# ==========================================================
# NORMALIZE CONTENT
# ==========================================================

def normalize_content(content):

    """
    Convert LangChain/Groq content into plain text.
    """

    if not content:

        return ""


    # ------------------------------------------------------
    # STRING
    # ------------------------------------------------------

    if isinstance(
        content,
        str
    ):

        return content


    # ------------------------------------------------------
    # LIST
    # ------------------------------------------------------

    if isinstance(content, list):

        text_parts = []

        for item in content:

            # ----------------------------------------------
            # DICT CONTENT
            # ----------------------------------------------

            if isinstance(item, dict):

                if "text" in item:

                    text_parts.append(str(item["text"]))

                elif "content" in item:

                    text_parts.append(str(item["content"]))

            # ----------------------------------------------
            # NORMAL CONTENT
            # ----------------------------------------------

            else:

                text_parts.append(str(item))


        return "".join(text_parts)


    # ------------------------------------------------------
    # FALLBACK
    # ------------------------------------------------------

    return str(content)


# ==========================================================
# STREAM CHAT
# ==========================================================

def stream_chat(user_input, thread_id, uploaded_context=""):

    """
    Stream the assistant response from LangGraph.

    Each text chunk is yielded to Streamlit immediately.
    """

    actual_message = build_actual_message(user_input, uploaded_context)


    # ======================================================
    # LANGGRAPH CONFIG
    # ======================================================

    config = {"configurable": {"thread_id": str(thread_id)}}


    # ======================================================
    # LANGGRAPH STREAM
    # ======================================================

    for message_chunk, metadata in chatbot.stream(

        {
            "messages": [HumanMessage(content=actual_message)]
        },

        config=config,

        stream_mode="messages"

    ):

        # --------------------------------------------------
        # ONLY AI MESSAGES
        # --------------------------------------------------

        if not isinstance(message_chunk, AIMessage):

            continue


        # --------------------------------------------------
        # GET CONTENT
        # --------------------------------------------------

        content = normalize_content(message_chunk.content)


        # --------------------------------------------------
        # SKIP EMPTY CHUNKS
        # --------------------------------------------------

        if not content:

            continue


        # --------------------------------------------------
        # YIELD CHUNK
        # --------------------------------------------------

        yield content