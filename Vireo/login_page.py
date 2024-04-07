import streamlit as st

def show_login_signup():
    """Display login and signup options."""
    st.markdown("""
                <div style="text-align: center";>
                <h1 style="font-size: 66px;"> Vireo 🌱 </hi>
                </div>
                """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    with tab1:
        st.header("Login")
        username_login = st.text_input("Username", key="login_username")
        password_login = st.text_input("Password", type="password", key="login_password")
        
        if st.button("Login"):
            if username_login in st.session_state.users and st.session_state.users[username_login] == password_login:
                st.session_state['authenticated'] = True
                st.session_state['username'] = username_login
                st.rerun()
            else:
                st.error("Incorrect Username or Password")

    with tab2:
        st.header("Sign Up")
        username_signup = st.text_input("Choose a Username", key="signup_username")
        password_signup = st.text_input("Choose a Password", type="password", key="signup_password")
        
        if st.button("Sign Up"):
            if username_signup in st.session_state.users:
                st.error("Username already exists. Please choose a different username.")
            elif username_signup and password_signup:
                st.session_state.users[username_signup] = password_signup
                st.success("You have successfully signed up. Please log in with your new credentials.")
            else:
                st.error("Username and password cannot be empty.")