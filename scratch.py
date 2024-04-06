import streamlit as st

# Placeholder for user database
users = {
    "solomon": "solomon1",
    "oladiran": "oladiran1",
    "robel": "robel1"
}

def login_page():
    """Function to display the login page and handle user authentication."""
    # Using session state to store user login status
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state['authenticated'] = True
            st.session_state['username'] = username  # Store the username in session state
        else:
            st.error("Incorrect Username/Password")
    
    return st.session_state['authenticated']

def main_app():
    """Function to display the main app content after successful login."""
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Environmental Impact Dashboard", "Carbon Footprint Calculator", "Contributions Page"])
    
    if page == "Home":
        st.title(f"Welcome to Vireo, {st.session_state['username']}!")
        st.write("Explore our features to start making a difference!")
        st.map()
    if page == 'Environmental Impact Dashboard':
        st.title('Env page')
    if page == 'Carbon Footprint Calculator':
        st.title('Carb page') 
    if page == 'Contributions Page':
        st.title('Contri page')

    # Implement other pages following the similar pattern

def main():
    """Main function to initialize the app."""
    if 'authenticated' not in st.session_state or not st.session_state['authenticated']:
        st.title("Vireo Login")
        authenticated = login_page()
        if authenticated:
            # Clear the login page
            st.experimental_rerun()
    else:
        main_app()

if __name__ == "__main__":
    main()
