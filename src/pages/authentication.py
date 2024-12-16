import streamlit as st

from .shush_excommunicado import show_shush_excom_page
from ..repositories import auth


def show_login_page():
    st.title("Login")
    user_id = st.text_input("ID")
    password = st.text_input("Password", type="password")
    login = st.button("Login")
    if login:
        # Авторизация
        user = auth.authenticate(user_id, password)  # Реализовать эту функцию
        if not user:
            st.warning("Invalid ID or password")
        elif auth.check_excommunicado(user["user_id"]):
            if "excom" not in st.session_state:
                st.session_state.excom = True
            show_shush_excom_page(user["user_id"])
        else:
            if 'user_id' not in st.session_state:
                st.session_state.user_id = user["user_id"]
            if 'role' not in st.session_state:
                st.session_state.role = user["role"]
            st.session_state.authed = True