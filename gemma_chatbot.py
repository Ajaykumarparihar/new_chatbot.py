# gemma_chatbot.py

import streamlit as st
import requests

# ✅ Your Groq API Key
GROQ_API_KEY = "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"

# ✅ Streamlit App Setup
st.set_page_config(page_title="Gemma Chatbot", layout="centered")
st.title("💎 Gemma-7b-It Chatbot (Groq)")
import streamlit as st
import requests

# 💡 IMPORTANT: Replace your key securely
GROQ_API_KEY = "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"

st.set_page_config(page_title="Groq Chatbot - Gemma", layout="centered")
st.title("🤖 Groq Chatbot using Gemma (7B-IT)")

# Initialize message history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

# Show past chat
for msg in st.session_state.messages[1:]:  # Skip system message in display
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
user_input = st.chat_input("💬 Ask anything...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Call Groq API
    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gemma-7b-it",
                "messages": st.session_state.messages,
                "temperature": 0.7
            }
        )

        if response.status_code == 200:
            data = response.json()
            reply = data["choices"][0]["message"]["content"]
            st.session_state.messages.append({"role": "assistant", "content": reply})
            with st.chat_message("assistant"):
                st.markdown(reply)
        else:
            st.error(f"❌ API Error {response.status_code}: {response.text}")

    except Exception as e:
        st.error(f"⚠️ Exception: {e}")

# ✅ Session State for Memory
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant powered by Gemma model."}]

# ✅ Display Previous Messages
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ✅ Chat Input
user_input = st.chat_input("Ask something...")

# ✅ On Prompt Send
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        thinking = st.empty()
        thinking.markdown("⏳ Thinking...")

        try:
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {GROQ_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gemma-7b-it",
                    "messages": st.session_state.messages,
                    "temperature": 0.7
                }
            )

            res_json = response.json()
            reply = res_json["choices"][0]["message"]["content"].strip()

            st.session_state.messages.append({"role": "assistant", "content": reply})
            thinking.markdown(reply)

        except Exception as e:
            thinking.markdown(f"❌ Error: {str(e)}")
