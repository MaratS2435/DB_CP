import streamlit as st
from ..directories import contracts_table


def show_manage_contracts_page():
    st.title("Contract page")

    display_option = st.radio("Choose option", ["Create", "Delete"])

    if display_option == "Create":
        description = st.text_input("Description")
        reward = st.number_input("Reward", min_value=10000, max_value=999999999, value=10000)
        task_name = st.text_input("Task name")

        if st.button("Create contract"):
            if not description or not reward:
                st.warning("Description and reward are required")
            else:
                try:
                    contracts_table.put_contract(description, reward, task_name)
                    st.success("Contract created successfully!")
                except Exception as e:
                    st.error(f"An error occurred: {e}")

    elif display_option == "Delete":
        contracts = contracts_table.my_contracts()
        contract_id = st.selectbox("Select contract to delete", contracts.keys())
        if st.button("Delete contract"):
            if not contract_id:
                st.warning("Please select a contract to delete")
            else:
                try:
                    contracts_table.delete_contract(contracts[contract_id])
                    st.success("Contract deleted successfully! We hope you got what you wanted")
                except Exception as e:
                    st.error(f"An error occurred: {e}")