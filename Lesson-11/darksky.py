"""

https://darksky.net/dev 

78b65883930875275cd338e25131cdee

"""
import requests

def get_coords(address):
    api_key = "AIzaSyDFuKg19Z_gzuOnKYa0JusiWFJZ6avhwn8"
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    response = requests.get(url, params={"address": address, "key": api_key})
    if response.status_code == 200:
        result = response.json()
        latlng = result["results"][0]["geometry"]["location"]
        return latlng
    return None

def get_weather_summary(lat, lng):
    url = "https://api.darksky.net/forecast/{}/{},{}"
    key = "78b65883930875275cd338e25131cdee"
    req_url = url.format(key, lat, lng)
    response = requests.get(req_url)
    if response.ok:
        current_weather_data = response.json()
        summary = current_weather_data["currently"]["summary"]
        return summary
    return "Error"


address = input("What is you city and state? ")
latlng = get_coords(address)
summary = get_weather_summary(latlng["lat"], latlng["lng"])

print("Your weather is currently: {}".format(summary))
