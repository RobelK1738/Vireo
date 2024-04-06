import streamlit as st

# Initialize session state for user database if it doesn't exist
if 'users' not in st.session_state:
    st.session_state['users'] = {
    "solomon": "solomon1",
    "oladiran": "oladiran1",
    "robel": "robel1"
}

def show_login_signup():
    """Function to display login and signup options."""
    st.title("Vireo - Sign In or Sign Up")

    # Tabs for Login and Signup
    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    with tab1:
        st.header("Login")
        username_login = st.text_input("Username", key="login_username")
        password_login = st.text_input("Password", type="password", key="login_password")
        
        if st.button("Login"):
            if username_login in st.session_state.users and st.session_state.users[username_login] == password_login:
                st.session_state['authenticated'] = True
                st.session_state['username'] = username_login
                st.experimental_rerun()
            else:
                st.error("Incorrect Username/Password")

    with tab2:
        st.header("Sign Up")
        username_signup = st.text_input("Choose a Username", key="signup_username")
        password_signup = st.text_input("Choose a Password", type="password", key="signup_password")
        
        if st.button("Sign Up"):
            if username_signup in st.session_state.users:
                st.error("Username already exists. Please choose a different username.")
            elif username_signup and password_signup:
                # Add the new user to the "database"
                st.session_state.users[username_signup] = password_signup
                st.success("You have successfully signed up. Please log in with your new credentials.")
            else:
                st.error("Username and password cannot be empty.")

def main_app():
    """Display the main application after successful login."""
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Environmental Impact Dashboard", "Carbon Footprint Calculator", "Contributions Page"])
    
    if page == "Home":
        st.title(f"Welcome to Vireo, {st.session_state['username']}!")
        st.write("Explore our features to start making a difference!")
    # Implement other pages here based on the project requirements

def main():
    """Main function to manage app flow based on login status."""
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False

    if st.session_state['authenticated']:
        main_app()
    else:
        show_login_signup()

if __name__ == "__main__":
    main()
