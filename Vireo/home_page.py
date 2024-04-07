import streamlit as st
import pydeck as pdk
sample_locations = {
    "New York": {"lat": 40.7128, "lon": -74.0060},
    "London": {"lat": 51.5074, "lon": -0.1278},
    "Tokyo": {"lat": 35.6895, "lon": 139.6917},
    "Paris": {"lat": 48.8566, "lon": 2.3522},
    "Berlin": {"lat": 52.5200, "lon": 13.4050},
    "Moscow": {"lat": 55.7558, "lon": 37.6173},
    "Sydney": {"lat": -33.8688, "lon": 151.2093},
    "Toronto": {"lat": 43.6532, "lon": -79.3832},
    "Rio de Janeiro": {"lat": -22.9068, "lon": -43.1729},
    "Beijing": {"lat": 39.9042, "lon": 116.4074},
    "Cairo": {"lat": 30.0444, "lon": 31.2357},
    "Dubai": {"lat": 25.2048, "lon": 55.2708},
    "Mumbai": {"lat": 19.0760, "lon": 72.8777},
    "Nairobi": {"lat": -1.286389, "lon": 36.817223},
    "Cape Town": {"lat": -33.9249, "lon": 18.4241},
    "Buenos Aires": {"lat": -34.6037, "lon": -58.3816},
    "Lagos": {"lat": 6.5244, "lon": 3.3792},
    "Jakarta": {"lat": -6.2088, "lon": 106.8456},
    "Seoul": {"lat": 37.5665, "lon": 126.9780},
    "Mexico City": {"lat": 19.4326, "lon": -99.1332},
    "Lima": {"lat": -12.0464, "lon": -77.0428},
    "Bangkok": {"lat": 13.7563, "lon": 100.5018},
    "Kuala Lumpur": {"lat": 3.1390, "lon": 101.6869},
    "Singapore": {"lat": 1.3521, "lon": 103.8198},
    "Manila": {"lat": 14.5995, "lon": 120.9842},
    "Hanoi": {"lat": 21.0285, "lon": 105.8542},
    "Bogota": {"lat": 4.7110, "lon": -74.0721},
    "Istanbul": {"lat": 41.0082, "lon": 28.9784},
    "Santiago": {"lat": -33.4489, "lon": -70.6693},
    "Athens": {"lat": 37.9838, "lon": 23.7275},
    "Copenhagen": {"lat": 55.6761, "lon": 12.5683},
    "Wellington": {"lat": -41.2865, "lon": 174.7762},
    "Helsinki": {"lat": 60.1699, "lon": 24.9384},
}


def fetch_environmental_data(lat, lon):
    """Fetch environmental data for the given latitude and longitude."""
    # Placeholder for actual data fetching logic
    return f"Environmental data for Latitude: {lat}, Longitude: {lon}\n- Climate: Placeholder\n- Air Quality: Placeholder"


def home_page():
    st.title(f"Welcome to Vireo, {st.session_state['username']}!")
    st.write("Select a location to see environmental data.")

    # Dropdown for selecting a location
    location = st.selectbox("Select a location:", list(sample_locations.keys()))

    # Display map centered on the selected location
    loc_data = sample_locations[location]
    view_state = pdk.ViewState(latitude=loc_data["lat"], longitude=loc_data["lon"], zoom=10)
    map = pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=view_state,
        layers=[],
    )
    st.pydeck_chart(map)

    # Button to fetch data for the selected location
    if st.button('Show Environmental Data'):
        data = fetch_environmental_data(loc_data["lat"], loc_data["lon"])
        st.write(data)
        
        

# def display_footer():
#     """Display the footer section with contact and social media information."""
#     footer_html = """
#     <hr style="border-top: 2px solid #bbb;">
#     <div style="text-align: center; padding: 10px;">
#         <p>Get in Touch:</p>
#         <a href="https://www.twitter.com/yoursoftware" target="_blank">Twitter</a> | 
#         <a href="https://www.facebook.com/yoursoftware" target="_blank">Facebook</a> | 
#         <a href="https://www.instagram.com/yoursoftware" target="_blank">Instagram</a>
#         <br>
#         <img src="URL_TO_YOUR_LOGO" style="width: 100px; margin-top: 10px;">
#         <p>Contact Us: <a href="mailto:contact@yoursoftware.com">contact@yoursoftware.com</a></p>
#     </div>
#     """
#     st.markdown(footer_html, unsafe_allow_html=True)