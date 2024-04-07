import streamlit as st
import pydeck as pdk
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json
import http.client

def parse_json_to_dict(json_str):
    return json.loads(json_str)

def city_search(city):
    if ' ' in city:
        city = city.replace(' ', '_')

    conn = http.client.HTTPSConnection("api.ambeedata.com")

    headers = {
        'x-api-key': "cd78b30f9b341e83643dbbc8defc14f23a6c1fa87faf51c8eedb78f44743a897",
        'Content-type': "application/json"
        }

    conn.request("GET", f"/latest/by-city?city={city}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    data = data.decode("utf-8")
    diction = parse_json_to_dict(data)
    cardiox = diction['stations'][0]['CO']
    air_cat = diction['stations'][0]['aqiInfo']['category']
    return cardiox

def show_temp(city_name):
    url = f"https://api.weatherbit.io/v2.0/current?city={city_name}&key=f6900071df1145afbe623bcf39dea538&unit=I"
    response = requests.get(url)

    #Means you have access to API server
    if response.status_code == 200:
        weather_data = response.json()
        if weather_data.get('data'):
            weather_data = weather_data['data'][0]
            temp_celsius = weather_data['app_temp']
            climate = weather_data['weather']['description']
            aq = weather_data['aqi']
            return (temp_celsius*(9/5) + 32), aq, climate
        else:
            return ("Weather data not found for this city.")
    else:
        return ("Error fetching weather data. Please try again later.")


with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
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

# Initialize session state for user database if it doesn't exist
if 'users' not in st.session_state:
    st.session_state['users'] = {
        "user1": "password1",
        "user2": "password2",
    }

# Sample locations dictionary remains unchanged
def firstDataRow(cardiox, climate):
    col1, col2= st.columns(2)
    col1.metric("Carbon Dioxied Emissions", f"{cardiox}", 0.134, delta_color="inverse")
    col2.metric("Scenery", f"{climate}")
    
def secDataRow(airq, temp):
    col1, col2= st.columns(2)
    col1.metric("Temp", f"{temp}  °F", f"{-(3.2)}  °F")
    col2.metric("Air Quality", f"{airq}", delta="Good")


def fetch_environmental_data(climate, temp, cardiox, airq):
    """Fetch environmental data for the given latitude and longitude."""
    secDataRow(airq, temp)
    firstDataRow(cardiox, climate)
    
    


def show_login_signup():
    """Display login and signup options."""
    st.title("Vireo - Sign In or Sign Up")

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
                st.error("Incorrect Username/Password")

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

def calculate(perishables, electronics, miscellaneous, mode, average_distance, utilities):
    # Emission factors
    perishables_factor = 0.3
    electronics_factor = 0.5
    miscellaneous_factor = 0.4
    transportation_factors = {
        "Car": 0.21,
        "Public Transport": 0.05,
        "Bike": 0,
        "Walk": 0,
        "Motorcycle": 0.12
    }
    utilities_factor = 0.2

    # Daily to yearly conversion factor
    days_per_year = 365

    # Calculate emissions for each category
    lifestyle_emissions = (perishables * perishables_factor) + \
                          (electronics * electronics_factor) + \
                          (miscellaneous * miscellaneous_factor)
    transportation_emissions = transportation_factors[mode] * average_distance * days_per_year
    housing_emissions = utilities * utilities_factor

    # Total yearly carbon footprint
    total_emissions = lifestyle_emissions + transportation_emissions + housing_emissions

    emissions_sources = {
        'Lifestyle': lifestyle_emissions,
        'Transportation': transportation_emissions,
        'Housing': housing_emissions
    }
    largest_source = max(emissions_sources, key=emissions_sources.get)

    suggestions = {
        'Lifestyle': (
            "It looks like your lifestyle choices are having a significant impact on your carbon footprint. "
            "Reducing consumption of perishables, electronics, and other goods can have a profound effect. "
            "Consider purchasing locally sourced food to decrease transportation emissions, opting for second-hand or refurbished electronics, "
            "and reducing waste by recycling. Small changes can make a big difference over time."
        ),
        'Transportation': (
            f"Transportation is a major part of your carbon footprint, particularly from {mode.lower()} commuting. "
            "If possible, switching to more sustainable modes like public transportation, biking, or walking can dramatically reduce your emissions. "
            "Carpooling is another great way to decrease your impact. Additionally, if you're in the market for a new vehicle, "
            "consider an electric or hybrid model to further decrease your transportation emissions."
        ),
        'Housing': (
            "Your home's energy use is a significant contributor to your carbon footprint. Investing in energy-efficient appliances, "
            "improving home insulation, and using renewable energy sources can all help reduce your emissions. Consider installing low-flow water fixtures "
            "to reduce hot water use and switching to LED lighting to decrease electricity consumption. "
            "Even small actions, like unplugging devices when not in use, can add up to substantial savings both for the planet and on your utility bills."
        )
    }

    suggestion = suggestions[largest_source]
    
    # Return both the total emissions and the suggestion
    return total_emissions / 1000, suggestion

def carbon_page():
    """Display the Carbon Footprint Calculator page with inputs for lifestyle, transportation, and housing."""
    st.title("CO2e Calculator")
    st.write("Enter details about you to calculate your carbon footprint")
    st.text("Lifestyle")
    perishables = st.text_input("Amount spent per year on perishables (e.g., food, drinks, pharmaceuticals)")
    electronics = st.text_input("Amount spent per year on electronics (e.g., TV, phones, subscriptions)")
    miscellaneous = st.text_input("Amount spent per year on miscellaneous (e.g., recreation, insurance, education)")

    st.text("Transportation")
    mode = st.selectbox("Mode of transportation", ["Car", "Public Transport", "Bike", "Walk", "Motorcycle"])
    average_distance = st.text_input("Average daily commute distance in km (e.g., 10)")
    
    st.text("Household")
    utilities = st.text_input("Amount spent per year on housing utilities (e.g., gas, water, electricity)")
    
    if st.button('Calculate my Carbon Footprint'):
        # Convert input strings to float; provide 0.0 as default if conversion fails
        perishables_val = float(perishables) if perishables.replace('.', '', 1).isdigit() else 0.0
        electronics_val = float(electronics) if electronics.replace('.', '', 1).isdigit() else 0.0
        miscellaneous_val = float(miscellaneous) if miscellaneous.replace('.', '', 1).isdigit() else 0.0
        average_distance_val = float(average_distance) if average_distance.replace('.', '', 1).isdigit() else 0.0
        utilities_val = float(utilities) if utilities.replace('.', '', 1).isdigit() else 0.0

        
        total_emissions_metric_tons, suggestion = calculate(
            perishables_val, electronics_val, miscellaneous_val, mode, average_distance_val, utilities_val
        )

        # Use the returned values to format the output message
        result_message = (
            f"Your estimated yearly carbon emissions: {total_emissions_metric_tons:.2f} metric tons of CO2e. "
            f"{suggestion}"
        )
        st.session_state['carbon_footprint_result'] = result_message
        st.write(result_message)


# The calculate, carbon_page, contributions_page, home_page, and display_footer functions remain unchanged
def contributions_page():
    st.title("Community")

    if 'events' not in st.session_state:
        st.session_state['events'] = [
            {"name": "Beach Cleanup", "activity": "Cleaning", "date": "2024-04-22", "location": "Santa Monica Beach"},
            {"name": "Tree Planting", "activity": "Planting", "date": "2024-05-05", "location": "Central Park"},
        ]

    tab1, tab2 = st.tabs(["Host an Effort", "Join an Effort"])

    with tab1:
        st.header("Host an Effort:")
        event_name = st.text_input("Event Name", key="new_event_name")
        activity_type = st.selectbox("Activity Type", ["Cleaning", "Planting", "Recycling"], key="new_activity_type")
        event_date = st.date_input("Date", key="new_event_date")
        event_location = st.text_input("Location", key="new_event_location")
        
        if st.button("Host an Effort"):
            new_event = {
                "name": event_name,
                "activity": activity_type,
                "date": event_date.strftime("%Y-%m-%d"),
                "location": event_location,
            }
            st.session_state['events'].append(new_event)
            email_subject = f"New Event Created: {event_name}"
            email_message = (
                f"You have created an event '{event_name}' on {event_date.strftime('%Y-%m-%d')}. "
                f"Activity: {activity_type}, Location: {event_location}. "
                "Thank you for contributing to a better environment!"
            )
            # send_email(email_subject, email_message, 'robiemelaku@gmail.com')
            st.success(f"Event '{event_name}' created successfully!")
            
            

    with tab2:
        st.header("Join an Effort")
        if st.session_state['events']:
            for event in st.session_state['events']:
                st.markdown(f"**{event['name']}**")
                st.markdown(f"- Activity: {event['activity']}")
                st.markdown(f"- Date: {event['date']}")
                st.markdown(f"- Location: {event['location']}")
                if st.button(f"Join {event['name']}", key=event['name']):
                    email_subject = f"Joined Event: {event['name']}"
                    email_message = (
                        f"You have joined the event '{event['name']}' on {event['date']}. "
                        f"Activity: {event['activity']}, Location: {event['location']}. "
                        "Details will be sent to your email. Thank you for participating!"
                    )
                    # send_email(email_subject, email_message, 'robiemelaku@gmail.com')
                    st.success(f"Thanks for joining {event['name']}! Further details will be sent to your email.")
                    
                    
        else:
            st.write("No events available at the moment. Consider creating one!")

def display_footer():
    """Display the footer section with contact and social media information."""
    footer_html = """
    <hr style="border-top: 2px solid #bbb;">
    <div style="text-align: center; padding: 10px;">
        <p>Get in Touch:</p>
        <a href="https://www.twitter.com/yoursoftware" target="_blank">Twitter</a> | 
        <a href="https://www.facebook.com/yoursoftware" target="_blank">Facebook</a> | 
        <a href="https://www.instagram.com/yoursoftware" target="_blank">Instagram</a>
        <br>
        <img src="URL_TO_YOUR_LOGO" style="width: 100px; margin-top: 10px;">
        <p>Contact Us: <a href="mailto:contact@yoursoftware.com">contact@yoursoftware.com</a></p>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)

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
        temp, airq, climate = show_temp(location)
        cardiox= city_search(location)
        fetch_environmental_data(climate, temp, cardiox, airq)
        
def main_app():
    """Display the main application after successful login."""
    home, tab2, tab3 = st.tabs(["Home", "CO2e Calculator", "Community"])

    with home:
        home_page()
    with tab2:
        carbon_page()
    with tab3:
        contributions_page()
    display_footer()

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
