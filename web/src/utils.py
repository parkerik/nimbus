import os

import service
import streamlit as st


def set_up() -> None:
    """Sets page title and layout"""
    st.set_page_config(
        page_title="Nimbus",
        page_icon="src/assets/favicon.png",
        layout="wide",
    )


def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if service.autheticate_user(
            st.session_state["username"], st.session_state["password"]
        ):
            del st.session_state["password"]
            st.session_state["password_correct"] = True
            st.session_state["user"] = st.session_state["username"]

    if st.session_state.get("password_correct", False):
        return True

    login_form()
    if "password_correct" in st.session_state:
        st.error("Incorrect username or password")
    return False
