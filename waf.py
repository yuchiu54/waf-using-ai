import os

from dotenv import load_dotenv
from flask import Flask, redirect, request, url_for
import requests

from detect import is_malicious

load_dotenv()
app = Flask(__name__)

@app.route("/waf", methods=["GET"])
def waf():
    data = request.args.to_dict()
    url = os.getenv("ORIGIN_SERVER")
    if len(data) == 0 or is_malicious(data.values()):
        return "<p> bad request"
    return redirect(url)

@app.route("/waf-shadow", methods=["GET"])
def waf_shadow():
   # this api will predict request data with multiple models
   # if result is better than live one then replace it with this

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
