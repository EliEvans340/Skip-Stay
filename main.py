# streamlit_app.py
import os
import shutil
import streamlit as st
def move_files(source_folder, dest_folder):
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        dest_path = os.path.join(dest_folder, filename)

        if os.path.isfile(source_path):
            shutil.move(source_path, dest_path)

def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        move_files('pages/hide', 'pages')
        return True

move_files('pages', 'pages/hide')
if check_password():
    st.write("Here goes your normal Streamlit app...")
    st.button("Click me")