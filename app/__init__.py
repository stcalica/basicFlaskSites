from flask import Flask
import json
import os
files = os.listdir(".")
print files

app = Flask(__name__, static_folder='static', static_url_path='')

with open("app/company.config.json", "r") as f:
	    config = json.load(f)

app.config.company = config["company"]
app.config.brand_image_url = config["brand_image_url"]

from app import routes
