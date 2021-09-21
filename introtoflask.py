# MVC (Model, View, Controllers) (General Web)
# MVT (Model, View, Template) (For Flask)
# HTTP, HTTPs (Hyper Text Transfer Protocol)
# GET, POST, PUT, Patch (API operations)
# HTTP response code RFC 1656
# 1.x
# 2.x
# 3.x
# 4.x
# 5.x

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Hello World</h1>'

# Creating Dynamic Routes
# http:127.0.0.1/kartik
# Bonjour, Kartik!

@app.route("/user/<name>")
def user(name):
    return "<h1>Bonjour, %s!</h1>" % name

# Headers
# You need to install a cross plugin cross to ensure smooth
# functionality on multiple web browsers
@app.route("/headers")
def headers():
    user_agent = request.headers.get('User-Agent')
    return "<p> You are currently browsing on %s </p>" % user_agent

if __name__ == '__main__':
    app.run(debug=True)

