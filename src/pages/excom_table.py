import pandas as pd
import streamlit as st
from ..directories import excommunicado

def show_excom_table():
    st.title("Excommunicados")
    st.write("Assisting excomunicado is prohibited. You have been warned")
    data = excommunicado.get_excommunicados()
    df = pd.DataFrame(data, columns=["Name", "Rule", "Reward", "Beginning"]).to_dict(orient="records")
    st.dataframe(df)