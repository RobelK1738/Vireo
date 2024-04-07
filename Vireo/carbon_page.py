import streamlit as st

def calculate(perishables, electronics, miscellaneous, mode, average_distance, utilities):
    # Emission factors
    perishables_factor = 0.3
    electronics_factor = 0.5
    miscellaneous_factor = 0.4
    transportation_factors = {
        "Car 🚘": 0.21,
        "Public Transport 🚍": 0.05,
        "Bike 🚴": 0,
        "Walk 🚶": 0,
        "Motorcycle 🏍️": 0.12
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
            f"Transportation is a major part of your carbon footprint, particularly from {mode.lower()[:len(mode)-1]} commuting. "
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
    st.markdown("""
                <div style="text-align: center";>
                <h1 style="font-size: 30px;"> CO2e Calculator 💨 </hi>
                </div>
                """, unsafe_allow_html=True)
    st.write("Enter details about you to calculate your carbon footprint")
    st.markdown("""
                <div>
                <h1 style="font-size: 20px;"> Lifestyle </hi>
                </div>
                """, unsafe_allow_html=True) 
    

    perishables = st.text_input("Amount spent per year on perishables (e.g., food, drinks, pharmaceuticals)")
    electronics = st.text_input("Amount spent per year on electronics (e.g., TV, phones, subscriptions)")
    miscellaneous = st.text_input("Amount spent per year on miscellaneous (e.g., recreation, insurance, education)")

    st.markdown("""
                <div>
                <h1 style="font-size: 20px;"> Transportation </hi>
                </div>
                """, unsafe_allow_html=True) 
    mode = st.selectbox("Mode of transportation", ["Car 🚘", "Public Transport 🚍", "Bike 🚴", "Walk 🚶", "Motorcycle 🏍️"])
    average_distance = st.text_input("Average daily commute distance in km (e.g., 10)")
    
    st.markdown("""
                <div>
                <h1 style="font-size: 20px;"> Household </hi>
                </div>
                """, unsafe_allow_html=True) 
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
            f"Your estimated yearly carbon emissions is {total_emissions_metric_tons:.2f} metric tons of CO2e. \n"
            
            f"\n{suggestion}"
        )
        st.session_state['carbon_footprint_result'] = result_message
        st.write(result_message)