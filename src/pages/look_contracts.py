from ..directories import contracts_table
import streamlit as st
import pandas as pd

def show_look_contracts_page():
    st.title("Join the fun!")

    option = st.radio("Choose option", ["All contracts", "Become executer"])

    contracts = contracts_table.get_contracts_table()

    if option == "All contracts":
        st.dataframe(pd.DataFrame(contracts, columns=["Contract ID", "Task", "Client", "Reward"]).to_dict(orient="records"))
    elif option == "Become executer":
        contract_id = st.number_input("Contract ID", min_value=1, value=1, step=1, format="%d")
        if st.button("Join contract"):
            try:
                contracts_table.make_executer(contract_id, st.session_state.user_id)
                st.write("You joined the contract successfully! There's no way back now")
            except Exception as e:
                st.error(f"An error occurred: {e}")