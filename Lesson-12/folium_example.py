# https://data.sfgov.org/api/views/ritf-b9ki/rows.csv?accessType=DOWNLOAD

import folium
from folium.plugins import MarkerCluster
import pandas as pd
import webbrowser

SF_COORDINATES = (37.76, -122.45)
crimedata = pd.read_csv('https://data.sfgov.org/api/views/9v2m-8wqu/rows.csv?accessType=DOWNLOAD')

# for speed purposes
MAX_RECORDS = 1000
 
# create empty map zoomed in on San Francisco
map = folium.Map(location=SF_COORDINATES, zoom_start=12)

marker_cluster = MarkerCluster(name="Crime").add_to(map)
# add a marker for every record in the filtered data, use a clustered view
for each in crimedata[0:MAX_RECORDS].iterrows():
    folium.Marker([each[1]['Y'], each[1]['X']]).add_to(marker_cluster)
 
filename = "test.html"
map.save(filename)
webbrowser.open(filename)