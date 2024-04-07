import streamlit as st
import http.client
import json
import requests
import pydeck as pdk

def firstDataRow(cardiox, climate):
    col1, col2= st.columns(2)
    col1.metric("Carbon Dioxied Emissions 💨", f"{cardiox}", 0.134, delta_color="inverse")
    col2.metric("Scenery 🏞️", f"{climate}")
    
def secDataRow(airq, temp):
    col1, col2= st.columns(2)
    col1.metric("Temp", f"{temp}  °F", f"{-(3.2)}  °F")
    col2.metric("Air Quality", f"{airq}", delta="Good")


def fetch_environmental_data(climate, temp, cardiox, airq):
    """Fetch environmental data for the given latitude and longitude."""
    secDataRow(airq, temp)
    firstDataRow(cardiox, climate)


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
            return round((temp_celsius*(9/5) +32), 2) , aq, climate
        else:
            return ("Weather data not found for this city.")
    else:
        return ("Error fetching weather data. Please try again later.")

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
    "Madrid": {"lat": 40.4168, "lon": -3.7038},
    "Rome": {"lat": 41.9028, "lon": 12.4964},
    "Vienna": {"lat": 48.2082, "lon": 16.3738},
    "Amsterdam": {"lat": 52.3676, "lon": 4.9041},
    "Brussels": {"lat": 50.8503, "lon": 4.3517},
    "Stockholm": {"lat": 59.3293, "lon": 18.0686},
    "Oslo": {"lat": 59.9139, "lon": 10.7522},
    "Lisbon": {"lat": 38.7223, "lon": -9.1393},
    "Warsaw": {"lat": 52.2297, "lon": 21.0122},
    "Budapest": {"lat": 47.4979, "lon": 19.0402},
    "Prague": {"lat": 50.0755, "lon": 14.4378},
    "Zurich": {"lat": 47.3769, "lon": 8.5417},
    "Hong Kong": {"lat": 22.3193, "lon": 114.1694},
    "Shanghai": {"lat": 31.2304, "lon": 121.4737},
    "Los Angeles": {"lat": 34.0522, "lon": -118.2437},
    "Chicago": {"lat": 41.8781, "lon": -87.6298},
    "Houston": {"lat": 29.7604, "lon": -95.3698},
    "Miami": {"lat": 25.7617, "lon": -80.1918},
    "San Francisco": {"lat": 37.7749, "lon": -122.4194},
    "Montreal": {"lat": 45.5017, "lon": -73.5673},
    "Vancouver": {"lat": 49.2827, "lon": -123.1207},
    "São Paulo": {"lat": -23.5505, "lon": -46.6333},
    "Buenos Aires": {"lat": -34.6037, "lon": -58.3816}, # Already in the list, added again by mistake
    "New Delhi": {"lat": 28.6139, "lon": 77.2090},
    "Karachi": {"lat": 24.8607, "lon": 67.0011},
    "Dhaka": {"lat": 23.8103, "lon": 90.4125},
    "Kolkata": {"lat": 22.5726, "lon": 88.3639},
    "Bangalore": {"lat": 12.9716, "lon": 77.5946},
    "Melbourne": {"lat": -37.8136, "lon": 144.9631},
    "Auckland": {"lat": -36.8485, "lon": 174.7633},
    "Brisbane": {"lat": -27.4698, "lon": 153.0251},
}

def display_footer():
    footer = """
    <body>
    <div class="footer-basic" style="background-color: rgba(240, 240, 240, 0.75); padding: 40px;border-radius: 20px; ">
        <footer>
            <div class="social" style="text-align:center; padding-bottom:25px;"><a styles="font-size:24px;width:40px;height:40px;line-height:40px;display:inline-block;text-align:center;border-radius:50%;border:1px solid #ccc;margin:0 8px;color:inherit;opacity:0.75;"href="#"><i class="icon ion-social-instagram"></i></a><a href="#"><i class="icon ion-social-snapchat"></i></a><a href="#"><i class="icon ion-social-twitter"></i></a><a href="#"><i class="icon ion-social-facebook"></i></a></div>
            <ul class="list-inline" style="padding:0; list-style:none; text-align:center; font-size:18px; line-height:1.6; margin-bottom:0;">
                <li class="list-inline-item" style="padding:0 10px;"><a style="color:hsla(320,40%,30%,.6); text-decoration:none; opacity:0.8;" href="#">About</a></li>
                <li class="list-inline-item" style="padding:0 10px;"><a style="color:hsla(320,40%,30%,.6); text-decoration:none; opacity:0.8;" href="#">Terms</a></li>
                <li class="list-inline-item" style="padding:0 10px;"><a style="color:hsla(320,40%,30%,.6); text-decoration:none; opacity:0.8;" href="#">Privacy Policy</a></li>
            </ul>
            <p class="copyright" style="margin-top:15px;text-align:center;font-size:13px;color:#aaa;margin-bottom:0;">Vireo © 2024</p>
        </footer>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/js/bootstrap.bundle.min.js"></script>
</body>
    """
    st.markdown(footer, unsafe_allow_html=True)

def home_page():
    welcome = f"🌱Welcome to Vireo, {st.session_state['username'][0].upper()}{st.session_state['username'][1:]}!🌱"
    st.markdown(f"""
                <div style="text-align: center";>
                <h1 style="font-size: 30px;"> {welcome} </hi>
                </div>
                """, unsafe_allow_html=True) 

    location = st.selectbox("Select a location 📍", list(sample_locations.keys()))

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
    if st.button('Show Environmental Data 📈'):
        temp, airq, climate = show_temp(location)
        cardiox= city_search(location)
        fetch_environmental_data(climate, temp, cardiox, airq)