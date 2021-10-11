#!/usr/bin/env python3
import urllib.request
import urllib.parse
import http.client
import json

try:
    url = "http://api.geonames.org/findNearbyJSON?formatted=true&lat=48.865618158309374&lng=2.344207763671875&fclass=P&fcode=PPLA&fcode=PPL&fcode=PPLC&username=luisakun&style=full"
    f = urllib.request.urlopen(url,timeout=30)
    djson = json.loads(f.read())
    print(djson)

except:
    print('Error al consultar datos')