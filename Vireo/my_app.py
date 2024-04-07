import streamlit as st
from home_page import home_page, display_footer
from carbon_page import carbon_page
from community_page import community_page


def my_app():
    """Display the main application after successful login."""
    
    home, tab2, tab3 = st.tabs(["Home 🏠", "CO2e Calculator 💨", "Community 🌏"], )
    
    with home:
        home_page()
    with tab2:
        carbon_page()
    with tab3:
        community_page()
    display_footer()