from app import app
from flask import render_template

@app.route('/')
def index():
	return render_template("index.html", company=app.config.company, brand_image_url=app.config.brand_image_url)

@app.route('/about')
def about():
	#a little snippet in each one
	return render_template("about.html", company=app.config.company, brand_image_url=app.config.brand_image_url)

@app.route('/contact')
def contact():
	#show all social media icons for each corresponding thing in social media
	return render_template("contact.html", company=app.config.company, brand_image_url=app.config.brand_image_url)

@app.route('/gallery')
def gallery():
	#create a grid of images
	return render_template("gallery.html", company=app.config.company, brand_image_url=app.config.brand_image_url)

@app.route('/team')
def team():
	#for each team member create a specific amount of "boxes"
	return render_template("team.html", company=app.config.company, brand_image_url=app.config.brand_image_url)

@app.route('/event')
def event():
	#for each team member create a specific amount of "boxes"
	return render_template("team.html", company=app.config.company, brand_image_url=app.config.brand_image_url)
