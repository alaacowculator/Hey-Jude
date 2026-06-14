import streamlit as st
from managers import UserManager

class AuthManager:
    def __init__(self, user_manager):
        self.user_manager = user_manager

    def login(self, username, password):
        if self.user_manager.authenticate(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.page = "Dashboard"
            return True
        return False

    def signup(self, username, password):
        if not username or not password:
            st.error("All fields required.")
            return False
        elif username in self.user_manager.users:
            st.error("Username already exists.")
            return False
        else:
            self.user_manager.add_user(username, password)
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.page = "Dashboard"
            return True
