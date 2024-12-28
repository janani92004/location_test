import streamlit as st
from streamlit_geolocation import streamlit_geolocation

# Streamlit app layout
st.title("Get User Location Using Streamlit Geolocation")
st.write("Click the button below to get your latitude and longitude:")

# Get the user's location
location = streamlit_geolocation()

# Check if location data is available
if location:
    latitude = location['latitude']
    longitude = location['longitude']
    st.write(f"Latitude: {latitude}, Longitude: {longitude}")
else:
    st.write("Location data not available. Please allow location access.")
