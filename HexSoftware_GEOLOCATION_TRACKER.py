# Import necessary libraries for phone number validation, geolocation, and mapping
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import folium
import webbrowser
from opencage.geocoder import OpenCageGeocode
from pyfiglet import Figlet

figlet = Figlet (font = 'epic')

# API key for OpenCage geocoding service
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key
key = os.getenv("key")
print(key)
# Function to validate phone number length
def number_validation(number):
    vaild_status = ""
    
    if len(number) < 10:
        vaild_status = "Please enter a valid number"
    else:
        vaild_status = "Valid number"
    
    return vaild_status

# Function to format phone number by ensuring it starts with a country code "+"
def number_format(number):
    if number[0] != '+':
        number = '+' + number
    else:
        number = number
    
    return number

# Function to get the location description of the phone number
def number_loca(number):
    check_number = phonenumbers.parse(number)
    global number_location 
    number_location = geocoder.description_for_number(check_number, "en")

    print("The current province (location) the number is located: "+ number_location)

# Function to get the service provider (carrier) of the phone number
def number_service_provider(number):
    service_provider = phonenumbers.parse(number)
    network_provider = carrier.name_for_number(service_provider, "en")
    print(f"The current network provider of the {number} is : {network_provider}")

# Function to get the coordinates and additional location details
def number_coordinates():
    geocoder = OpenCageGeocode(key)
    # Use the location string to query geocode API
    qurey = str(number_location)
    request = geocoder.geocode(qurey)
    
    latitude = request[0]['geometry']['lat']
    longitude = request[0]['geometry']['lng']
    result = geocoder.reverse_geocode(latitude, longitude)
    
    print("Latitude: " + str(latitude) + "\nLongitude: " + str(longitude))

    print("Country code: " + result[0]['annotations']['flag'])
    print("Timezone: " + result[0]['annotations']['timezone']['name'] + " and the current day: " + result[0]['annotations']['timezone']['short_name'])

    # Create and save a map with the location marked as a marke
    map_loactaion = folium.Map(location=[latitude, longitude], zoom_start=10)
    folium.Marker([latitude, longitude], popup=number_location).add_to(map_loactaion)
    map_loactaion.save("Location.html")

    return "Location.html"

print(figlet.renderText("Welcome to Simon's Geolocation Tracker\nMake sure to start the number with the counrty code of the number e.g +27"))

# Get user input for the phone number to track
number = input("Enter the cell phone number you would like to track? ")

number_validation(number)
number_format(number)
number_loca(number)
number_service_provider(number)
number_coordinates()

# Open the generated map in a new web browser tab
webbrowser.open_new_tab("Location.html")


