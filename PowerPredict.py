# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 21:44:24 2021

@author: m
"""


# flask server virtual environment
# Adapted- https://github.com/ianmcloughlin/random-app/blob/master/rando.py

# 
# when server is running access on web browser at - http://127.0.0.1:5000

# import flask
from flask import Flask

# import keras and add model

from tensorflow import keras
model = keras.models.load_model("linearmodel.pkl")

# Form a new web app.
#app = fl.Flask(__name__)  - alternative way to create a new app
app = Flask(__name__, static_url_path='', static_folder='static')


# Root is PowerProduction.html
@app.route("/")
def root():
  return app.send_static_file('PowerProduction.html')

# Returns power value input by user (GET method)
# Received response 200 - http://127.0.0.1:5000
# tested with curl
# --------------------------------------------------------------------------------------------------

@app.route('/forecast/<int:x>', methods=['GET'])
@app.route('/forecast/<float:x>', methods=['GET'])
def forecast(x):
  forecast = model.forecast([x])
  #return 
  return str(forecast[0][0])
