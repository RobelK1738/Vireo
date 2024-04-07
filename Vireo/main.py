import streamlit as st
from my_app import my_app
from login_page import show_login_signup



with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
if 'users' not in st.session_state:
    st.session_state['users'] = {
        "user1": "password1",
        "user2": "password2",
    }
def main():
    """Main function to manage app flow based on login status."""
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False

    if st.session_state['authenticated']:
        my_app()
    else:
        show_login_signup()

if __name__ == "__main__":
    main()