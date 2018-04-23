from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webdb.db'
db = SQLAlchemy(app)



import folium
import requests
import pandas as pd
import matplotlib.pyplot as plt

api_key = "YOUR KEY"

url = "https://maps.googleapis.com/maps/api/geocode/json"

@app.route("/")
def main():
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


class Widget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    quantity = db.Column(db.Integer(), default=0)

    def __repr__(self):
        return '<Widget %r>' % self.nane

@app.route("/widgets", methods=['GET'])
def widgets():
    widgets = Widget.query.all()
    return render_template("widgets.html", widgets=widgets)

@app.route("/add_widget", methods=['POST'])
def add_widget():
    widget = Widget(name=request.form["name"], quantity=int(request.form["quantity"]))
    db.session.add(widget)
    db.session.commit()
    return redirect("/widgets")



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)