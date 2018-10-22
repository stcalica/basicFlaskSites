from flask import Flask
import os, json

app = Flask(__name__)

with open("app/company.config.json", "r") as f:
	config = json.load(f)

app.config.company = config["company"]
app.config.brand_image_url = config["brand_image_url"]
app.config.contact = config["contact"]
app.config.team = config["team"]

from app import routes
