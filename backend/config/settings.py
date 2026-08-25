import os
from dotenv import load_dotenv


load_dotenv()


HF_REPO_ID = os.getenv("HF_REPO_ID", "Qwen/Qwen2.5-72B-Instruct")

HF_TASK = os.getenv("HF_TASK", "text-generation")

MAX_DOCUMENT_SIZE_MB = int(os.getenv("MAX_DOCUMENT_SIZE_MB", "10"))

MAX_DOCUMENT_CHARS = int(os.getenv("MAX_DOCUMENT_CHARS", "50000"))

MAX_HISTORY_MESSAGES = int(os.getenv("MAX_HISTORY_MESSAGES", "20"))