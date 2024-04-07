import streamlit as st
from vireo_app import vireo_app
from login_page import show_login_signup
def main():
    """Main function to manage app flow based on login status."""
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False

    if st.session_state['authenticated']:
        vireo_app()
    else:
        show_login_signup()
if __name__ == "__main__":
    main()