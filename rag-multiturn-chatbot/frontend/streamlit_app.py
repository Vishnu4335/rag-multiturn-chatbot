import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

st.title("Company Policy RAG Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask a question")

if prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    try:

        response = requests.post(
            API_URL,
            json={"question": prompt}
        )

        data = response.json()

        # show backend error directly
        if "error" in data:

            st.error(data["error"])

        else:

            answer = data["answer"]

            citations = data["citations"]

            citation_text = "\n\n### Citations\n"

            for c in citations:
                citation_text += f"- {c}\n"

            final_answer = answer + citation_text

            with st.chat_message("assistant"):
                st.markdown(final_answer)

            st.session_state.messages.append({
                "role": "assistant",
                "content": final_answer
            })

    except Exception as e:

        st.error(f"Connection Error: {str(e)}")