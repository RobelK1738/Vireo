import streamlit as st
import pydeck as pdk

# Initialize session state for user database if it doesn't exist
if 'users' not in st.session_state:
    st.session_state['users'] = {
        "user1": "password1",
        "user2": "password2",
    }


# Sample locations for demonstration
# Expanded sample locations with additional global cities
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

def carbon_footprint_calculator():
    """Display the Carbon Footprint Calculator page."""
    st.title("Carbon Footprint Calculator")
    st.write("Enter details about your lifestyle to calculate your carbon footprint.")
    
    # Example input fields for lifestyle choices
    transportation = st.radio("How do you usually commute?", ["Drive", "Public Transport", "Bike", "Walk"])
    energy_use = st.slider("Rate your household energy use from 1 (low) to 10 (high)", 1, 10, 5)
    diet = st.selectbox("Select your diet type", ["Vegetarian", "Vegan", "Meat Eater"])
    lifestyle_details = st.text_area("Describe any other relevant lifestyle details")
    
    # Button to calculate the carbon footprint
    if st.button('Calculate Carbon Footprint'):
        # Placeholder for the prediction logic
        st.session_state['carbon_footprint_result'] = "Your estimated carbon footprint is XX metric tons of CO2 per year."
        st.write(st.session_state['carbon_footprint_result'])

def contributions_page():
    """Display the Contributions page for event creation and participation."""
    st.title("Contributions")

    # Simulated event storage (would be a database in a real app)
    if 'events' not in st.session_state:
        st.session_state['events'] = [
            {"name": "Beach Cleanup", "activity": "Cleaning", "date": "2024-04-22", "location": "Santa Monica Beach"},
            {"name": "Tree Planting", "activity": "Planting", "date": "2024-05-05", "location": "Central Park"},
        ]

    tab1, tab2 = st.tabs(["Create Event", "Participate"])

    with tab1:
        st.header("Create a New Environmental Event")
        event_name = st.text_input("Event Name")
        activity_type = st.selectbox("Activity Type", ["Cleaning", "Planting", "Recycling"])
        event_date = st.date_input("Date")
        event_location = st.text_input("Location")
        
        if st.button("Create Event"):
            # Add the new event to the session state
            st.session_state['events'].append({
                "name": event_name,
                "activity": activity_type,
                "date": event_date.strftime("%Y-%m-%d"),  # Format the date as a string
                "location": event_location,
            })
            st.success(f"Event '{event_name}' created successfully!")

    with tab2:
        st.header("Volunteer for an Event")
        if st.session_state['events']:
            # Display existing events
            for event in st.session_state['events']:
                st.markdown(f"**{event['name']}**")
                st.markdown(f"- Activity: {event['activity']}")
                st.markdown(f"- Date: {event['date']}")
                st.markdown(f"- Location: {event['location']}")
                if st.button(f"Join {event['name']}", key=event['name']):
                    st.success(f"Thanks for joining {event['name']}! Further details will be sent to your email.")
        else:
            st.write("No events available at the moment. Consider creating one!")

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

def main_app():
    """Display the main application after successful login."""
    home, tab2, tab3 = st.tabs(["Home", "Carbon Footprint Calculator", "Contributions Page"])

    with home:
        home_page()
    with tab2:
        carbon_footprint_calculator()
    with tab3:
        contributions_page()
    # Additional pages would go here...

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