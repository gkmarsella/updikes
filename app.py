from flask import Flask, render_template, request, redirect, url_for
from flask_modus import Modus
import os

app = Flask(__name__)
api = Modus(app)

maps_key = app.config['GOOGLEMAPS'] = os.environ.get('GOOGLEMAPS')

@app.route('/', methods=[ "GET"])
def search():
    return render_template("home.html", maps_key=maps_key)

if os.environ.get('ENV') == 'production':
    debug = False
else:
    debug = True

if __name__ == '__main__':
    app.run(debug=debug,port=3000)