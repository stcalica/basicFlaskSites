from flask import Flask
import json
import os

app = Flask(__name__)

with open("app/company.config.json", "r") as f:
	    config = json.load(f)

with open("app/events.config.json", "r") as f:
	    events = json.load(f)

with open("app/team.config.json", "r") as f:
	    team = json.load(f)

app.config.company = config["company"]
app.config.brand_image_url = config["brand_image_url"]
app.config.events = events
app.config.team = team

print app.config.company
print app.config.team
print app.config.events

from app import routes
