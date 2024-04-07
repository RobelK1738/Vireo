import streamlit as st
import re


def validate_password(password):
    """Check if the password meets the criteria: at least 8 characters, contains a digit and a special character."""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."
    return True, ""

def show_login_signup():
    """Function to display login and signup options with enhanced features."""
    st.title("Vireo")

    # Initialize user database structure in session state if not exists
    if 'users' not in st.session_state:
        st.session_state['users'] = {}

    tab2, tab1 = st.tabs(["Sign Up", "Log In"])
    

    with tab1:
        st.header("Login")
        username_login = st.text_input("Username", key="login_username")
        password_login = st.text_input("Password", type="password", key="login_password")
        
        if st.button("Login"):
            user_info = st.session_state.users.get(username_login)
            if user_info and user_info['password'] == password_login:
                st.session_state['authenticated'] = True
                st.session_state['username'] = username_login
                st.experimental_rerun()
            else:
                st.error("Incorrect Username/Password")

    with tab2:
        st.header("Sign Up")
        username_signup = st.text_input("Username", key="signup_username")
        email_signup = st.text_input("Email", key="signup_email")
        password_signup = st.text_input("Enter a Password", type="password", key="signup_password")
        password_valid, password_message = validate_password(password_signup)
        
        if st.button("Sign Up"):
            if username_signup in st.session_state.users:
                st.error("Username already exists. Please choose a different username.")
            elif not password_valid:
                st.error(password_message)
            elif username_signup and email_signup and password_signup:
                # Add the new user with email to the "database"
                st.session_state.users[username_signup] = {
                    'email': email_signup,
                    'password': password_signup
                }
                st.success("You have successfully signed up. Please log in with your new credentials.")
            else:
                st.error("Please fill in all fields.")