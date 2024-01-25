import os

from dotenv import load_dotenv
from flask import Flask, redirect, request, url_for, jsonify
import requests

from src.detect import is_malicious
from src.detect import Detector

load_dotenv()
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    # this api will hadle request include extracting payloads in request, 
    data = request.args.to_dict()
    # assigning payloads to live api and shadow api with requests
#    response = requests.post({"http://localhost:5000/live"}, payloads = data)
#    response = requests.post({"http://localhost:5000/shadow"}, payloads = data)
    return "<p> home"

@app.route("/live", methods=["GET"])
def live():
    # implement model in models folder
    data = request.args.to_dict()
    url = os.getenv("ORIGIN_SERVER")
    if len(data) == 0 or is_malicious(data.values()):
        return "<p> bad request"
    # if not poisonous
        # update_models
    return redirect(url)

@app.route("/shadow", methods=["GET"])
def shadow():
   # update models
   # performance check
   # if performance of model is better live than update models in models folder
   pass

@app.route("/test", methods=["GET"])
def test():
    # load model
    data = request.args.to_dict()
    if len(data) == 0 or is_malicious(data.values()):
        print("malforme payload founded")
        return "<p> bad request"
    print("pass WAF")
    return "<p> test page"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
