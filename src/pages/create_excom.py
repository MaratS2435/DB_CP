from ..directories import excommunicado
import streamlit as st

@st.cache_data
def show_rules():
    rules = excommunicado.get_rules()
    return {rule["description"]: rule["rule_id"] for rule in rules}


def show_create_excom_page():
    st.title("Manage excommunicados")
    rules = show_rules()

    option = st.radio("Choose option", ["Create excommunicado", "Edit excommunicado reward", "Delete excommunicado"])

    if option == "Create excommunicado":
        user_id = st.number_input("User ID", min_value=1, value=1, step=1)
        chosen_rule = st.selectbox("Rule ID", rules.keys())
        reward = st.number_input("Reward", min_value=10000, max_value=999999999, value=10000, step=1000)
        begining = st.date_input("Beginning")

        if st.button("Create excommunicado"):
            if not user_id or not chosen_rule or not reward or not begining:
                st.warning("Please fill all fields")
            else:
                try:
                    if excommunicado.put_excommunicado(user_id, rules[chosen_rule], reward, begining) == 1:
                        st.warning("User is already excommunicated")
                    elif excommunicado.put_excommunicado(user_id, rules[chosen_rule], reward, begining) == 2:
                        st.warning("User doesn't exist")
                    else:
                        st.success("Excommunicado created successfully!")
                except Exception as e:
                    st.error(f"An error occurred: {e}")

    elif option == "Edit excommunicado reward":
        user_id = st.number_input("User ID", min_value=1, value=1, step=1)
        new_reward = st.number_input("New reward", min_value=10000, max_value=999999999, value=10000, step=1000)

        if st.button("Edit excommunicado reward"):
            if not user_id or not new_reward:
                st.warning("Please fill all fields")
            else:
                try:
                    if excommunicado.edit_excommunicado_reward(user_id, new_reward):
                        st.warning("User isn't excommunicated")
                    else:
                        st.success("Reward updated successfully!")
                except Exception as e:
                    st.error(f"An error occurred: {e}")

    elif option == "Delete excommunicado":
        user_id = st.number_input("User ID", min_value=1, value=1, step=1)

        if st.button("Delete excommunicado"):
            if not user_id:
                st.warning("Please fill all fields")
            else:
                try:
                    if excommunicado.delete_excommunicado(user_id):
                        st.warning("User isn't excommunicated")
                    else:
                        st.success("Excommunicado deleted successfully!")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
