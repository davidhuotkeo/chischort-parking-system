import json
import os

with open("app/static/json/data.json", "r") as raw_json:
    data = json.load(raw_json)

service_parking = data["service"]
database = data["db"]
social = data["social"]

login_username = os.environ.get("CHISCHORT_USERNAME")
login_password = os.environ.get("CHISCHORT_PASSWORD")
