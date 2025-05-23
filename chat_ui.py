import streamlit as st

def render_chat(chat_history: list):
    st.markdown("""
    <style>
      .chat-container { display:flex; flex-direction:column; }
      .user-msg { background:#262730; padding:10px; border-radius:15px 0 15px 15px; margin-left: 50px; text-align:right; margin-bottom: 6px; }
      .bot-msg  { background:#0B0E12; padding:10px; border-radius:0 15px 15px 15px; margin-right: 25px; margin-bottom: 16px; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    for msg in reversed(chat_history):
        st.markdown(f"<div class='user-msg'>{msg['user']}</div>", unsafe_allow_html=True)

        if msg["type"] == "Código de programación":
            st.code(msg["bot"], language="python")
        else:
            st.markdown(f"<div class='bot-msg'>{msg['bot']}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
