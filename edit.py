#!/usr/bin/env python3
from flask import Flask, request
from make import make_leaflet
import webbrowser
app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/building', methods=('POST', ))
def building():
    print(request.form['title'])
    stadtteil = request.form['stadtteil'].title()
    title = request.form['title']
    coords = request.form['coords']
    filename = 'data/buildings/stadt/'+stadtteil+'-'+title.replace('-', ' ').title().replace(' ', '')
    try:
        open(filename, 'r')
    except:
        pass
    else:
        return ''

    f = open(filename, 'w')
    f.write(title+'\n'+coords+'\n\nKeine Notizen.\n')
    f.close()

    make_leaflet()
    return 'ok'

make_leaflet()

app.run(debug=True)
