import streamlit as st
from home_page import home_page
from carbon_page import carbon_page
from community_page import community_page
# from login_page import display_footer



# with open('styles.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
def vireo_app():
    if 'users' not in st.session_state:
        st.session_state['users'] = {
            "Robel": "Etunat@1738",
            "Solomon": "Solomon@1",
            "Oladiran": 'Oladiran@1',
            "Sharon": "Sharon@1"
        }
    home, tab2, tab3 = st.tabs(["Home", "CO2e Calculator", "Community"])
    with home:
        home_page()
    with tab2:
        carbon_page()
    with tab3:
        community_page()
    # display_footer()