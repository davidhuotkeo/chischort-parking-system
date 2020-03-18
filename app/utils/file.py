import json

with open("app/static/json/data.json", "r") as raw_json:
    data = json.load(raw_json)

service_parking = data["service"]
database = data["db"]
social = data["social"]
