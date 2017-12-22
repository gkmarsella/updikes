from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/', methods=[ "GET"])
def search():
    return render_template("home.html")

if os.environ.get('ENV') == 'production':
    debug = False
else:
    debug = True

if __name__ == '__main__':
    app.run(debug=debug,port=3000)