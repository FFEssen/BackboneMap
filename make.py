#!/usr/bin/env python3
import os

buildings_dir = './data/buildings/'
buildings_color = {'stadt': '#FF0000'}


#L.polygon([[51.460852,6.945248],[51.458285,6.957264],[51.449942,6.953487],[51.450905,6.946106]], { weight: 0, fillColor: '#ff0000', fillOpacity: 0.4 }).addTo(map).bindPopup("I am a polygon.");
def make_leaflet():
    add = []

    buildingsdir = './data/buildings/'
    for (dirpath, dirnames, filenames) in os.walk('./data/buildings/'):
        for filename in filenames:
            data = open(os.path.join(dirpath, filename)).read()
            title, latlng, description = data.split('\n', 2)
            add.append("L.polygon(%s, {weight: 0, fillColor: '%s', fillOpacity: 0.4}).addTo(map).bindPopup('<strong>%s</strong><br><br>%s');" % (latlng, buildings_color[dirpath[len(buildingsdir):]], title, description.strip().replace('\n', '<br>')))

    open('index.html', 'w').write(open('index.tpl.html').read().replace('/* add */', '\n'.join(add)))

if __name__ == '__main__':
    make_leaflet()
