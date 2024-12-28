import streamlit as st
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Function to get location using Selenium
def get_location_with_selenium():
    # Set up the Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode (no GUI)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open the local HTML file
    driver.get("locationtest_html.html")  # Update this path

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
st.write("Click the button below to get your latitude and longitude:")

# Button to get location
if st.button("Get Location"):
    latitude, longitude = get_location_with_selenium()
    if latitude and longitude:
        st.write(f"Latitude: {latitude}, Longitude: {longitude}")
    else:
        st.write("Could not retrieve location.")
