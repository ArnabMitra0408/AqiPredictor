import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import pickle
import json
from geopy.geocoders import Nominatim
from flask import Flask, request, render_template
import xgboost
app = Flask(__name__)

xgb_model = pickle.load(open('xgb_clf.pkl', "rb"))
scaler = pickle.load(open('scaler.pkl', "rb"))
API_KEY = "d9be5b1607992d9c2eb10dcafe8f42e2"
base_url = "http://api.openweathermap.org/data/2.5/air_pollution?"


def complete_url(n):
    url = base_url + "lat=" + str(n.latitude) + \
        "&lon=" + str(n.longitude)+'&appid='+API_KEY
    return url


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        nom = Nominatim(user_agent="Mon_Application")
        place = request.form["Place"]
        n = nom.geocode(place)
        url = complete_url(n)
    response = requests.get(url)
    data = response.json()
    co = data['list'][0]['components']['co']
    no = data['list'][0]['components']['no']
    no2 = data['list'][0]['components']['no2']
    o3 = data['list'][0]['components']['o3']
    so2 = data['list'][0]['components']['so2']
    pm2_5 = data['list'][0]['components']['pm2_5']
    pm10 = data['list'][0]['components']['pm10']
    nh3 = data['list'][0]['components']['nh3']
    features = [co, no, no2, o3, so2, pm2_5, pm10, nh3]
    scaled_features = scaler.transform(np.array(features).reshape(1, -1))
    aqi = int(xgb_model.predict(scaled_features))
    return render_template("index.html", answer=aqi)


if __name__ == "__main__":
    app.run(debug=True)
