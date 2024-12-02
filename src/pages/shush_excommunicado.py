import streamlit as st
from ..directories import excommunicado


def show_shush_excom_page():
    st.title("You are excommunicado")
    st.write('<span style="color:red;">Don\'t try to hide. Your days are numbered.</span>', unsafe_allow_html=True)

    data = excommunicado.get_excommunicado(st.session_state.user_id)
    if data is not None:
        st.write(f"Description: {data[0]}")
        st.write(f"Reward: {data[1]}")
        st.write(f"Begining: {data[2]}")