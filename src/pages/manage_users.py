import streamlit as st
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

from ..directories import users
from ..directories import hotels_affilations

@st.cache_data
def show_hotels():
    hotels = hotels_affilations.get_hotels()
    return {hotel["place"]: hotel["hotel_id"] for hotel in hotels}

@st.cache_data
def show_affilations():
    affilations = hotels_affilations.get_affilations()
    affilations.append({"name": None, "affilation_id": None})
    return {affilation["name"]: affilation["affilation_id"] for affilation in affilations}

def show_manage_users_page():
    st.title("Manage users")

    users_table = users.get_users()
    option = st.radio("Choose option", ["All users", "Register user", "Edit user"])

    if option == "All users":
        st.dataframe(pd.DataFrame(users_table, columns=["ID", "Name", "Age", "Status", "Role", "Hotel", "Affilation"]).to_dict(orient="records"))

    elif option == "Register user":
        hotels = show_hotels()
        affilations = show_affilations()
        name = st.text_input("Name")
        password = st.text_input("Password")
        age = st.number_input("Age", min_value=10, max_value=100, value=20, step=1)
        status = st.selectbox("Status", ["alive", "dead", "retired"])
        role = st.selectbox("Role", ["manager", "killer", None])
        hotel_id = st.selectbox("Hotel", hotels.keys())
        affilation_id = st.selectbox("Affilation", affilations.keys())

        if st.button("Register user"):
            if not name or not password or not age or not status or not hotel_id:
                st.warning("Please fill name, password, age, status and hotel")
            else:
                try:
                    new_id = users.put_user(name, password, age, status, role, hotel_id, affilation_id)
                    st.success("User registered successfully!")
                    st.write(f"User ID: {new_id}  Password: {password}")
                    st.write("Be sure to give the user their data!")
                except Exception as e:
                    st.error(f"An error occurred: {e}")


    elif option == "Edit user":
        user_id = st.number_input("User ID", min_value=1, value=1, step=1)
        option = st.selectbox("Option", ["status", "role", "hotel_id", "affilation_id"])
        new_value = st.text_input("New value")

        if st.button("Edit user"):
            if not option or not new_value or not user_id:
                st.warning("Please fill in all fields")
            else:
                try:
                    users.edit_user(user_id, option, new_value)
                    st.success("User edited successfully!")
                except Exception as e:
                    st.error(f"An error occurred: {e}")