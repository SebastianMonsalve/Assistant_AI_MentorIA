import streamlit as st
from prompt_builder import _prompt
from chat_ui import render_chat
from apiAI import generate

st.set_page_config(page_title="MentorIA", page_icon="🤖", layout="centered")

options = [
    "Personalizado",
    "Código de programación",
    "Post para X",
    "Post para Facebook",
    "Historia de Instagram",
    "Guion para TikTok",
    "Resumen de texto",
    "Correo profesional",
    "Idea de negocio",
    "Descripción de producto",
    "Traducción"
]

if "chat" not in st.session_state:
    st.session_state.chat = []

st.markdown("### Bienvenid@ a tu Asistente MentorIA🤖")
option_selected = st.selectbox("Tipo de contenido", options)

with st.form("form_prompt", clear_on_submit=True):
    prompt = st.text_input("¿En qué puedo ayudarte hoy?", placeholder="Pregunta lo que quieras...")
    enviar = st.form_submit_button("➡ Generar")

    if enviar and prompt:
        prompt_formateado = _prompt(prompt, option_selected)
        with st.spinner("Procesando..."):
            respuesta = generate(prompt_formateado)
            st.session_state.chat.append({"user": prompt, "bot": respuesta, "type": option_selected})

st.divider()
render_chat(st.session_state.chat)
