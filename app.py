import streamlit as st
from prompt_builder import construir_prompt
from chat_ui import render_chat
from apiAI import generar

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

st.markdown("### Bienvenid@ al Asistente MentorIA🤖")
option_selected = st.selectbox("Tipo de contenido", options)

with st.form("form_prompt", clear_on_submit=True):
    prompt = st.text_input("¿En qué puedo ayudarte hoy?", placeholder="Pregunta lo que quieras...")
    enviar = st.form_submit_button("➡ Enviar")

    if enviar and prompt:
        prompt_formateado = construir_prompt(prompt, option_selected)
        with st.spinner("Procesando..."):
            respuesta = generar(prompt_formateado)
            st.session_state.chat.append({"user": prompt, "bot": respuesta, "type": option_selected})

st.divider()
render_chat(st.session_state.chat)
