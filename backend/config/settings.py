

import os

from dotenv import load_dotenv


load_dotenv()

def get_groq_api_key():

    # Streamlit Cloud
    try:
        if "GROQ_API_KEY" in st.secrets:
            return st.secrets["GROQ_API_KEY"]
    except Exception:
        pass

    # Local .env
    return os.getenv("GROQ_API_KEY")


GROQ_API_KEY = get_groq_api_key()

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY is not configured."
    )



MAX_DOCUMENT_SIZE_MB = int(os.getenv("MAX_DOCUMENT_SIZE_MB", "10"))

MAX_DOCUMENT_CHARS = int(os.getenv("MAX_DOCUMENT_CHARS", "50000"))

MAX_HISTORY_MESSAGES = int(os.getenv("MAX_HISTORY_MESSAGES", "20"))