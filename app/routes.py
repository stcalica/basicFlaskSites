from app import app
from flask import render_template

#read a config file from the server to display each company specifics

@app.route('/')
def index():
	return render_template("index.html", company=app.config.company, brand_image_url=app.config.brand_image_url)

@app.route('/contact')
def contact():
	return render_template("contact.html", company=app.config.company, brand_image_url=app.config.brand_image_url)

@app.route('/about')
def about():
	return render_template("about.html", company=app.config.company, brand_image_url=app.config.brand_image_url)
