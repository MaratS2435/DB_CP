import streamlit as st
from ..directories import excommunicado

def show_excom_table():
    st.title("Excommunicados")
    st.write("Assisting excomunicado is prohibited. You have been warned")
    data = excommunicado.get_excommunicados()
    st.dataframe(data)