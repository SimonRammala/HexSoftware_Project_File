import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import folium
from opencage.geocoder import OpenCageGeocode
from keys import key



number = "+27676056036"

check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")
print(number_location)

service_provider = phonenumbers.parse(number)
network_provider = carrier.name_for_number(service_provider, "en")
print(network_provider)


geocoder = OpenCageGeocode(key)
qurey = str(number_location)
request = geocoder.geocode(qurey)
latitude = request[0]['geometry']['lat']
longitude = request[0]['geometry']['lng']
result = geocoder.reverse_geocode(latitude, longitude)
print("Country code " + result[0]['annotations']['flag'])


map_loactaion = folium.Map(location=[latitude, longitude], zoom_start=10)
folium.Marker([latitude, longitude], popup=number_location).add_to(map_loactaion)
map_loactaion.save("Location.html")
print("Location.html saved")


