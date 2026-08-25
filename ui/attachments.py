

import streamlit as st

from services.document_service import process_uploaded_file, load_http_file, build_document_context

from utils.session_state import clear_attachment


# ==========================================================
# RENDER ATTACHMENT MENU
# ==========================================================

def render_attachment_menu():

    with st.popover( "➕", use_container_width=True):

        st.markdown( "### 📎 Add to chat")

        # --------------------------------------------------
        # FILE
        # --------------------------------------------------

        uploaded_file = st.file_uploader("Upload document", type=["pdf", "docx", "txt"], key="document_uploader")

        if uploaded_file:

            if st.button("📎 Attach File", use_container_width=True):

                with st.spinner("Processing document..."):

                    text = process_uploaded_file(uploaded_file)

                st.session_state["uploaded_context"] = build_document_context(text, uploaded_file.name, "file")

                st.session_state["uploaded_file_name"] = uploaded_file.name

                st.session_state["uploaded_source"] = "file"

                st.success("Document attached.")

                st.rerun()

        st.divider()

        # --------------------------------------------------
        # URL
        # --------------------------------------------------

        st.markdown("### 🌐 Attach from URL")

        url = st.text_input("HTTP/HTTPS URL", placeholder=("https://example.com/file.pdf"), key="http_file_url")

        if st.button( "🌐 Attach URL", use_container_width=True):

            if not url.strip():

                st.warning("Please enter a URL.")

            else:

                with st.spinner("Loading document..."):

                    text = load_http_file(url.strip())

                st.session_state["uploaded_context"] = build_document_context(text, url.strip(), "url")

                st.session_state["uploaded_file_name"] = url.strip()

                st.session_state["uploaded_source"] = "url"

                st.success("URL attached.")

                st.rerun()

        # --------------------------------------------------
        # REMOVE
        # --------------------------------------------------

        if st.session_state["uploaded_context"]:

            st.divider()

            st.info("📎 Document attached.")

            if st.button("❌ Remove attachment", use_container_width=True):

                clear_attachment()

                st.rerun()