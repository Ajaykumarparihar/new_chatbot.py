import streamlit as st
import requests

# ✅ Your Groq API key
GROQ_API_KEY = "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"

# ✅ Streamlit UI settings
st.set_page_config(page_title="Groq Chatbot", layout="centered")
st.title("🤖 Groq Chatbot using llama3‑8b‑8192")

# ✅ Message history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# ✅ Add system-level instruction for a smarter response
SYSTEM_PROMPT = {
    "role": "system",
    "content": "You are a friendly assistant, continuously learning from the conversation to provide better answers."
}

if len(st.session_state.messages) == 0:
    st.session_state.messages.append(SYSTEM_PROMPT)

# ✅ Display previous messages (chat history)
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ✅ User input for chat
user_input = st.chat_input("Ask me anything...")

# ✅ Handling the input from user
if user_input:
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # ✅ Make API call to Groq for response
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama3-8b-8192",  # ✅ Correct model name
            "messages": st.session_state.messages,
            "temperature": 0.7
        }
    )

    # ✅ Handle Groq response
    if response.status_code == 200:
        result = response.json()
        bot_reply = result["choices"][0]["message"]["content"]

        # Append assistant reply to chat history
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})

        with st.chat_message("assistant"):
            st.markdown(bot_reply)

    else:
        st.error(f"❌ Error {response.status_code}: {response.text}")

# ✅ Add feature to clear chat history
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.experimental_rerun()

# ✅ Option to download entire chat as text
if st.download_button("📄 Download chat", "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages]), file_name="chat.txt"):
    st.success("Downloaded!")
