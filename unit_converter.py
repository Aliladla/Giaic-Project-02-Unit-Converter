import streamlit as st

# Function to convert units based on input values and units
def convert_units(value, unit_from, unit_to):
    # Dictionary that holds conversion rates for different unit pairs
    conversions = {
        "meters_kilometers": 0.001,      # 1 meter = 0.001 kilometer
        "kilometers_meters": 1000,       # 1 kilometer = 1000 meters
        "grams_kilograms": 0.001,        # 1 gram = 0.001 kilogram
        "kilograms_grams": 1000          # 1 kilogram = 1000 grams
    }

    # Creating the conversion key based on the units selected by the user
    key = f"{unit_from}_{unit_to}"

    # Checking if the key exists in the conversions dictionary
    if key in conversions:
        # If the conversion exists, perform the conversion
        conversion = conversions[key]
        return value * conversion
    else:
        # If conversion is not supported, return an error message
        return "Conversion not supported"

# Title of the Streamlit app
st.title("Unit Converter")

# Input field for the user to enter the value they want to convert
value = st.number_input("Enter the value:",min_value=3.0,step=3.0)

# Dropdown menu for selecting the unit to convert from
unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"])

# Dropdown menu for selecting the unit to convert to
unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

# Button to trigger the conversion when clicked
if st.button("Convert"):
    # Call the convert_units function to get the result
    result = convert_units(value, unit_from, unit_to)
    # Display the converted value
    st.write(f"Converted value: {result}")
