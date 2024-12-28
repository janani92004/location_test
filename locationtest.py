import streamlit as st
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Function to get location using Selenium
def get_location_with_selenium():
    # Set up the Selenium WebDriver with headless options
    options = Options()
    options.add_argument('--headless')  # Run in headless mode (no GUI)
    options.add_argument('--no-sandbox')  # Bypass OS security model
    options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open the local HTML file
    driver.get("locationtest.html")  # Update this path

    # Click the "Get Location" button
    get_location_button = driver.find_element(By.ID, "getLocationBtn")
    get_location_button.click()

    # Wait for the location to be retrieved
    time.sleep(2)  # Adjust this time as needed

    # Extract latitude and longitude from the output paragraph
    location_output = driver.find_element(By.ID, "locationOutput").text
    driver.quit()

    # Parse the latitude and longitude from the output
    if "Latitude:" in location_output:
        lat_lon = location_output.split(", ")
        latitude = lat_lon[0].split(": ")[1]
        longitude = lat_lon[1].split(": ")[1]
        return latitude, longitude
    else:
        return None, None

# Streamlit app layout
st.title("Get User Location")
st.write("Click the button below to search for hospitals or medical shops nearby:")

# Initialize session state for location data if not already done
if 'location_data' not in st.session_state:
    st.session_state['location_data'] = {'latitude': None, 'longitude': None}

# Button to search for hospitals
if st.button("Search For Hospitals Nearby"):
    latitude, longitude = get_location_with_selenium()
    if latitude and longitude:
        st.session_state['location_data']['latitude'] = latitude
        st.session_state['location_data']['longitude'] = longitude
        st.write(f"Latitude: {latitude}, Longitude: {longitude}")
        # Here you can add the logic to search for hospitals using the latitude and longitude
    else:
        st.write("Could not retrieve location.")

# Button to search for medical shops
if st.button("Search For Medical Shops Nearby"):
    latitude, longitude = get_location_with_selenium()
    if latitude and longitude:
        st.session_state['location_data']['latitude'] = latitude
        st.session_state['location_data']['longitude'] = longitude
        st.write(f"Latitude: {latitude}, Longitude: {longitude}")
        # Here you can add the logic to search for medical shops using the latitude and longitude
    else:
        st.write("Could not retrieve location.")

# Display the current location data if available
if st.session_state['location_data']['latitude'] and st.session_state['location_data']['longitude']:
    st.write(f"Current Location - Latitude: {st.session_state['location_data']['latitude']}, Longitude: {st.session_state['location_data']['longitude']}")
