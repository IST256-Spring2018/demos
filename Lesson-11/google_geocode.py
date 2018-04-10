"""

http://maps.googleapis.com/maps/api/geocode/json?address=...&key=...

AIzaSyDFuKg19Z_gzuOnKYa0JusiWFJZ6avhwn8

"""

import requests

api_key = "AIzaSyDFuKg19Z_gzuOnKYa0JusiWFJZ6avhwn8"

url = "https://maps.googleapis.com/maps/api/geocode/json"

address = input("What is you city and state? ")

response = requests.get(url, params={"address": address, "key": api_key})

if response.status_code == 200:
    result = response.json()
    latlng = result["results"][0]["geometry"]["location"]
    print(latlng)