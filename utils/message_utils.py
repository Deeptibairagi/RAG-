

from langchain_core.messages import HumanMessage, AIMessage, ToolMessage


# ==========================================================
# NORMALIZE AI CONTENT
# ==========================================================

def normalize_ai_content(content):

    if not content:

        return ""

    if isinstance(content, list):

        text_parts = []

        for item in content:

            if isinstance(item, dict):

                if "text" in item:

                    text_parts.append(str(item["text"]))

            else:

                text_parts.append(str(item))

        return "\n".join(text_parts)

    return str(content)


# ==========================================================
# CONVERT MESSAGES
# ==========================================================

def convert_messages_for_ui(messages):

    result = []

    for message in messages:

        if isinstance(message, HumanMessage):

            content = str(message.content)

            if "USER QUESTION:" in content:

                content = content.split("USER QUESTION:", 1 )[1].strip()

                content = ("📎 **Document attached**\n\n" + content)

            result.append({"role": "user", "content": content})

        elif isinstance(message, AIMessage):

            content = normalize_ai_content(message.content)

            if not content:
                continue

            result.append({"role": "assistant", "content": content})

        elif isinstance(message, ToolMessage):

            continue

    return result