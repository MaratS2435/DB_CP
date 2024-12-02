from ..directories import excommunicado
import streamlit as st

def show_rules():
    rules = excommunicado.get_rules()
    return {rule["description"]: rule["rule_id"] for rule in rules}


def show_create_excom_page():
    st.title("Create excommunicado")
    rules = show_rules()

    user_id = st.number_input("User ID")
    chosen_rule = st.selectbox("Rule ID", rules.keys())
    reward = st.number_input("Reward")
    begining = st.date_input("Begining")

    if st.button("Create excommunicado"):
        if not user_id or not rule_id or not reward or not begining:
            st.warning("Please fill all fields")
        else:
            excommunicado.put_excommunicado(user_id, rules[chosen_rule], reward, begining)
