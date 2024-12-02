import streamlit as st
from pandas import to_datetime

from ..directories import excommunicado


def show_shush_excom_page(user_id):
    st.title("You are excommunicado")
    st.write('<span style="color:red;">Don\'t try to hide. Your days are numbered.</span>', unsafe_allow_html=True)

    data = excommunicado.get_excommunicado(user_id)
    if data is not None:
        st.write(f"Description: {data[0]}")
        st.write(f"Reward: {data[1]}")
        st.write(f"Beginning: {data[2]}")