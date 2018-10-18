from app import app
from flask import render_template

#read a config file from the server to display each company specifics

@app.route('/')
def index():
	return render_template("index.html", company=app.config.company, brand_image_url=app.config.brand_image_url)

@app.route('/team')
def team():
	return render_template("team.html", company=app.config.company, brand_image_url=app.config.brand_image_url, team=app.config.team)

@app.route('/events')
def events():
	return render_template("events.html", company=app.config.company, brand_image_url=app.config.brand_image_url, events=app.config.events)
