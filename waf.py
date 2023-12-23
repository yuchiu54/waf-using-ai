import os

from dotenv import load_dotenv
from flask import Flask, redirect, request, url_for
import requests

from detect import is_benign

load_dotenv()
app = Flask(__name__)

@app.route("/", methods=["GET"])
def waf():
    data = request.args.to_dict()
    url = os.getenv("ORIGIN_SERVER")
    if is_benign():
        response = requests.post(url, json=data)
        if response.status_code != 200:
            return "<p> Fail to send request to service. Try again later"
    else:
        return redirect(url_for("bad_request"))
    return "<p>This is waf route"

@app.route("/bad_request")
def bad_request():
    return "<p>This is a bad request"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
