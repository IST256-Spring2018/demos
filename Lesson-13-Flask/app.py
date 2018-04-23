from flask import Flask, render_template, request
app = Flask(__name__)

import folium
import requests
import pandas as pd
import matplotlib.pyplot as plt

api_key = "YOUR KEY"

url = "https://maps.googleapis.com/maps/api/geocode/json"

@app.route("/")
def main():
    return "Hello World!"
    return render_template("index.html")

@app.route('/map', methods=['POST'])
def map():
    address = request.form['address']
    response = requests.get(url, params={"address": address, "key": api_key})
    if response.status_code == 200:
        result = response.json()
        latlng = result["results"][0]["geometry"]["location"]

        map = folium.Map(location=(latlng["lat"], latlng["lng"]), zoom_start=20)
        marker = folium.Marker((latlng["lat"], latlng["lng"]))
        map.add_child(marker)
        map.save("templates/map.html")
        return render_template('map.html')
    else:
        return render_template('badinput.html')

@app.route("/visualize", methods=['GET'])
def visualize():
    sh = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/master/superhero/superhero-movie-dataset-1978-2012.csv')
    sh.columns = [ 'year', 'title', 'comic', 'imdb', 'rt', 'composite', 'opening_weeked_bo', 'avg_ticket_price', 'opening_weekend_attend', 'us_pop_that_year']
    sample_plot = sh.plot.bar(x ='year', y ='opening_weekend_attend', title="Opening Week Attendence" )
    plt.savefig('static/viz.png')
    return render_template('viz.html')



if __name__ == "__main__":
    app.run(debug=True)