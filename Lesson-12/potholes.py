import folium
import pandas as pd
import webbrowser

SYR = (43.0481, -76.1474)
map = folium.Map(location=SYR, zoom_start=14)

data = pd.read_csv('https://cityofsyracuse.github.io/RoadsChallenge/data/potholes.csv')
print(data.sample(5))

SYR = (43.0481, -76.1474)
map = folium.Map(location=SYR, zoom_start=14)
subset = data.sample(500)
for row in subset.to_records():
    coords = (row['Longitude'],row['Latitude'])
    loc = str(row['strLocation']) + ' ' + str(row['dtTime'])
    marker = folium.CircleMarker(location=coords, radius=15, popup=loc,color='#3186cc',fill_color='#3186cc')
    map.add_child(marker)
    
filename = "potholes.html"
map.save(filename)
webbrowser.open(filename)