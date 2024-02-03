import os

from dotenv import load_dotenv
from flask import Flask, redirect, request, url_for, jsonify
import requests

from detect import Detector
from analysis import analysis

load_dotenv()
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
#    url = request.url
#    payloads = url.split("?")[1]
    return redirect(url_for(".live", **request.args))

@app.route("/live", methods=["GET"])
def live():
    data = request.args.to_dict()
    url = os.getenv("ORIGIN_SERVER")
    detector = Detector()
    if data != {}:
        is_malicious = detector.detect(data.values())
        detector.record()
        if is_malicious:
            return "<p> bad request"
    return redirect(url)

@app.route("/shadow", methods=["GET"])
def shadow():
    # monitor and analysis
    data = request.args.to_dict()
    anaysis()
    return "<p> shadow"

@app.route("/test", methods=["GET"])
def test():
    data = request.args.to_dict()
    detector = Detector()
    is_malicious = detector.detect(data.values())
    detector.record()
    if is_malicious:
        print("malformed payload founded")
        return "<p> bad request"
    print("pass WAF")
    return "<p> test page"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
