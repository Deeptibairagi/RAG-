

from langchain_groq import ChatGroq

from config.settings import GROQ_API_KEY, GROQ_MODEL


# ==========================================================
# GROQ CHAT MODEL
# ==========================================================


def create_chat_model():
    llm = ChatGroq(model=GROQ_MODEL, temperature=0, groq_api_key=GROQ_API_KEY)

    return llm



# ==========================================================
# APPLICATION MODEL
# ==========================================================

chat_model = create_chat_model()