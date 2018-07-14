from flask import Flask, jsonify, render_template
from newsapi.articles import Articles
from newsapi.sources import Sources
import requests

app = Flask(__name__)
a = Articles(API_KEY="867af1dffb80450b9770b4bcc10c8e14")
s = Sources(API_KEY="867af1dffb80450b9770b4bcc10c8e14")


@app.route("/<user>")
def homepage(user):
	return render_template("Welcome.html", name=user)

@app.route("/headlines")
def headlines():
	data =  a.get_by_latest("the-verge")
	article = data["articles"]
	#return jsonify(article)
	return render_template("Headlines.html",list=article,title="TOP HEADLINES")

@app.route("/general")
def general():
	data =  s.get_by_category("general")
	article = data["sources"]
	#return jsonify(data)
	return render_template("Display.html",list=article,title="GENERAL NEWS")

@app.route("/technical")
def tech():
	data = s.get_by_category("technology")
	article = data["sources"]
	return render_template("Display.html",list=article,title="TECHNICAL NEWS")

"""@app.route("/sports")
def sports():
	data = {
	'title': "SPORTS NEWS",
	'content': s.get_by_category("sport")

	}
	return jsonify(data)"""

@app.route("/business")
def business():
	data = s.get_by_category("business")
	article = data["sources"]
	return render_template("Display.html",list=article,title="BUSINESS NEWS")

@app.route("/entertainment")
def entertainment():
	data = s.get_by_category("entertainment")
	article = data["sources"]
	return render_template("Display.html",list=article,title="ENTERTAINMENT NEWS")

# @app.route("/science")
# def science():
# 	data = s.get_by_category("science-and-nature")
# 	article = data["sources"]
# 	return render_template("Display.html",list=article,title="SCIENCE AND NATURE NEWS")

"""@app.route("/gaming")#, methods=['POST'])
def gaming():
	data = {
	'title': "GAMING NEWS",
	'content': s.get_by_category("gaming")

	}
	return jsonify(data)"""


if __name__=='__main__':
	app.run(host='0.0.0.0', debug=True)