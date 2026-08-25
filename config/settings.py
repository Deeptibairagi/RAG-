# import os

# from dotenv import load_dotenv


# # ==========================================================
# # LOAD ENVIRONMENT
# # ==========================================================

# load_dotenv()


# # ==========================================================
# # APPLICATION
# # ==========================================================

# APP_TITLE = "Personal Chatbot"

# APP_ICON = "🤖"



# # ==========================================================
# # GROQ
# # ==========================================================

# GROQ_API_KEY = os.getenv("GROQ_API_KEY")



# # ==========================================================
# # ALPHA VANTAGE
# # ==========================================================

# ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")


# # ==========================================================
# # MODEL
# # ==========================================================

# GROQ_MODEL = os.getenv("GROQ_MODEL")


# # ==========================================================
# # DATABASE
# # ==========================================================

# DATABASE_PATH = os.getenv("DATABASE_PATH", "data/chatbot.db")


# # ==========================================================
# # DOCUMENT
# # ==========================================================

# MAX_DOCUMENT_SIZE_MB = int(os.getenv("MAX_DOCUMENT_SIZE_MB", "10"))


# # ==========================================================
# # VALIDATE REQUIRED CONFIG
# # ==========================================================


# if not GROQ_API_KEY:
#     raise ValueError("GROQ_API_KEY is not configured.")



import os

from dotenv import load_dotenv


# ==========================================================
# LOAD ENVIRONMENT
# ==========================================================

load_dotenv()


# ==========================================================
# APPLICATION
# ==========================================================

APP_TITLE = "Personal Chatbot"

APP_ICON = "🤖"


# ==========================================================
# GROQ
# ==========================================================

GROQ_API_KEY = os.getenv(
    "GROQ_API_KEY"
)


# ==========================================================
# ALPHA VANTAGE
# ==========================================================

ALPHA_VANTAGE_API_KEY = os.getenv(
    "ALPHA_VANTAGE_API_KEY"
)


# ==========================================================
# MODEL
# ==========================================================

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "llama-3.3-70b-versatile"
)


# ==========================================================
# DATABASE
# ==========================================================

# Get project root:
#
# config/settings.py
#        ↑
# parent directory = project root
#

PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)


DATABASE_PATH = os.getenv(
    "DATABASE_PATH",
    os.path.join(
        PROJECT_ROOT,
        "data",
        "chatbot.db"
    )
)


# ==========================================================
# DOCUMENT
# ==========================================================

MAX_DOCUMENT_SIZE_MB = int(
    os.getenv(
        "MAX_DOCUMENT_SIZE_MB",
        "10"
    )
)


# ==========================================================
# VALIDATE REQUIRED CONFIG
# ==========================================================

if not GROQ_API_KEY:

    raise ValueError(
        "GROQ_API_KEY is not configured."
    )