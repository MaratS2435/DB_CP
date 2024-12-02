from ..directories import executers
from ..directories import contracts_table
import streamlit as st

def show_executers_page():
    contracts = contracts_table.my_contracts()
    contract_id = st.selectbox("Select contract", contracts.keys())
    if st.button("Show executers"):
        try:
            executers_table = executers.get_executers(contracts[contract_id])
            if executers_table is None:
                st.warning("No executers found")
            else:
                st.dataframe(executers_table)
        except Exception as e:
            st.error(f"An error occurred: {e}")