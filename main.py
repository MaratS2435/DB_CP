import streamlit as st
from src.directories import auth
from src.pages.authentication import show_login_page
from src.pages.create_delete_contract import show_manage_contracts_page
from src.pages.look_contracts import show_look_contracts_page
from src.pages.manage_users import show_manage_users_page
from src.pages.create_excom import show_create_excom_page
from src.pages.look_executers import show_executers_page
from src.pages.shush_excommunicado import show_shush_excom_page
from src.pages.excom_table import show_excom_table


def main():
    st.title("Continental")

    if "authed" not in st.session_state:
        show_login_page()

    else:
        if st.session_state.role == "manager":
            st.sidebar.title("What do you want to do?")
            page = st.sidebar.radio(
                "Choose an option",
                ["Manage users", "Manage excommunicados"],
            )
            if page == "Manage users":
                show_manage_users_page()
            elif page == "Manage excommunicados":
                show_create_excom_page()

        elif st.session_state.role == "killer":
            st.sidebar.title("Что вы хотите сделать?")
            page = st.sidebar.radio(
                "Choose an option",
                ["Manage contracts", "Available contracts", "Excommunicados"],
            )
            if page == "Manage contracts":
                show_manage_contracts_page()
            elif page == "Available contracts":
                show_look_contracts_page()
            elif page == "Excommunicados":
                show_excom_table()
        else:
            st.sidebar.title("Что вы хотите сделать?")
            page = st.sidebar.radio(
                "Choose an option",
                ["Manage contracts", "Excommunicados"],
            )
            if page == "Manage contracts":
                show_manage_contracts_page()
            elif page == "Excommunicados":
                show_excom_table()


if __name__ == "__main__":
    main()
