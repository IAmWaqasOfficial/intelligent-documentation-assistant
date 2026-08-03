import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

# ---------------------------------------
# Page Configuration
# ---------------------------------------

st.set_page_config(
    page_title="Intelligent Documentation Assistant",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Intelligent Documentation Assistant")
st.write("Upload a technical document and chat with it using AI.")

# ---------------------------------------
# Session State
# ---------------------------------------

if "filename" not in st.session_state:
    st.session_state.filename = None

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------------------
# Sidebar
# ---------------------------------------

with st.sidebar:

    st.header("📄 Upload Document")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        st.write(f"**Selected File:** {uploaded_file.name}")

        if st.button("Upload Document"):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    "application/pdf"
                )
            }

            try:

                response = requests.post(
                    f"{API_URL}/upload",
                    files=files
                )

                if response.status_code == 200:

                    data = response.json()

                    st.session_state.filename = data["filename"]

                    # Clear previous chat when a new document is uploaded
                    st.session_state.messages = []

                    st.success("Document uploaded successfully!")

                    st.write(
                        f"Chunks Created: {data['chunks']}"
                    )

                else:

                    st.error("Upload failed.")

            except Exception as e:

                st.error(f"Backend Error:\n{e}")

    st.divider()

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []

        st.rerun()

# ---------------------------------------
# Main Screen
# ---------------------------------------

if st.session_state.filename:

    st.success(
        f"Current Document: {st.session_state.filename}"
    )

else:

    st.info(
        "Upload a PDF from the sidebar to begin."
    )

# ---------------------------------------
# Display Previous Messages
# ---------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ---------------------------------------
# Chat Input
# ---------------------------------------

if st.session_state.filename:

    question = st.chat_input(
        "Ask something about your document..."
    )

    if question:

        # -----------------------------
        # Show User Message
        # -----------------------------

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):

            st.markdown(question)

        payload = {
            "filename": st.session_state.filename,
            "question": question
        }

        try:

            with st.chat_message("assistant"):

                with st.spinner("Thinking..."):

                    response = requests.post(
                        f"{API_URL}/ask",
                        json=payload
                    )

                    if response.status_code == 200:

                        data = response.json()

                        answer = data.get(
                            "answer",
                            "No answer generated."
                        )

                        st.markdown(answer)

                        with st.expander(
                            "View Retrieved Chunks"
                        ):

                            for i, chunk in enumerate(
                                data["relevant_chunks"],
                                start=1
                            ):

                                st.markdown(
                                    f"**Chunk {i}**"
                                )

                                st.write(chunk)

                                st.divider()

                        st.session_state.messages.append(
                            {
                                "role": "assistant",
                                "content": answer
                            }
                        )

                    else:

                        st.error(
                            "Failed to get response from backend."
                        )

        except Exception as e:

            st.error(
                f"Backend Error:\n{e}"
            )