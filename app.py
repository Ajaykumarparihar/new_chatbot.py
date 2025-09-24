import streamlit as st
import requests

# ✅ Your Groq API key
GROQ_API_KEY = "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"

# ✅ Streamlit UI settings
st.set_page_config(page_title="Groq Chatbot", layout="centered")
st.title("🤖 Groq Chatbot using llama-3.1-8b-instant")

# ✅ Message history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# ✅ Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ✅ User input
user_input = st.chat_input("Ask me anything...")

if user_input:
    # Add user message to session
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # ✅ Make API call to Groq
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.1-8b-instant",  # ✅ Updated model name
            "messages": st.session_state.messages,
            "temperature": 0.7
        }
    )

    # ✅ Handle Groq response
    if response.status_code == 200:
        result = response.json()
        bot_reply = result["choices"][0]["message"]["content"]

        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        with st.chat_message("assistant"):
            st.markdown(bot_reply)
    else:
        st.error(f"❌ Error {response.status_code}: {response.text}")
