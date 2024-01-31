import os

from dotenv import load_dotenv
from flask import Flask, redirect, request, url_for, jsonify
import requests

from detect import Detector

load_dotenv()
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    url = request.url
    payloads = url.split("?")
    response = requests.get(f"http://localhost:5000/live?{payloads}")
    response = requests.get(f"http://localhost:5000/shadow?{payloads}")
    return "<p> home"

@app.route("/live", methods=["GET"])
def live():
    data = request.args.to_dict()
    url = os.getenv("ORIGIN_SERVER")
    detector = Detector()
    if detector.detect(data.values()):
        return "<p> bad request"
    return redirect(url)

@app.route("/shadow", methods=["GET"])
def shadow():
    data = request.args.to_dict()
    detector = Detector()
    return "<p> shadow"

@app.route("/test", methods=["GET"])
def test():
    data = request.args.to_dict()
    detector = Detector()
    if len(data) == 0 or detector.detect(data.values()):
        print("malforme payload founded")
        return "<p> bad request"
    print("pass WAF")
    return "<p> test page"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
