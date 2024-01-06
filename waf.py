import os

from dotenv import load_dotenv
from flask import Flask, redirect, request, url_for
#from flask import flask_request
import requests

from detect import is_malicious

load_dotenv()
app = Flask(__name__)

@app.route("/", methods=["GET"])
def waf():
    data = request.args.to_dict()
    url = os.getenv("ORIGIN_SERVER")

    if len(data) == 0 or is_malicious(data.values()):
        return "<p> bad request"

    response = requests.post(url, json=data)
    if response.status_code != 200:
        return "<p> Fail to send request to service. Try again later"

@app.route("/bad_request")
def bad_request():
    return "<p>This is a bad request"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
