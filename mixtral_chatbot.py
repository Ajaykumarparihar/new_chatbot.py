# mixtral_bot.py
import streamlit as st
import requests

GROQ_API_KEY = "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"
MODEL = "mixtral-8x7b-8k"

st.set_page_config(page_title="Mixtral Chatbot", layout="centered")
st.title("⚡ Mixtral‑8x7b‑Instruct via Groq")

if "msgs" not in st.session_state:
    st.session_state.msgs = [{"role": "system", "content": "You are a helpful assistant."}]

for m in st.session_state.msgs[1:]:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

user_input = st.chat_input("Ask something...")

if user_input:
    st.session_state.msgs.append({"role": "user", "content": user_input})
    st.chat_message("user").markdown(user_input)

    try:
        resp = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"},
            json={"model": MODEL, "messages": st.session_state.msgs, "temperature": 0.7},
        )
        if resp.status_code == 200:
            data = resp.json()
            reply = data["choices"][0]["message"]["content"].strip()
            st.session_state.msgs.append({"role": "assistant", "content": reply})
            st.chat_message("assistant").markdown(reply)
        else:
            st.error(f"❌ {resp.status_code}: {resp.text}")
    except Exception as e:
        st.error("⚠️ " + str(e))
