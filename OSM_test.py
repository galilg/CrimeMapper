#!/usr/bin/env

import folium


geo_path = r'multi.json'
the_map = folium.Map([41.83, -88.70])
the_map.choropleth(geo_path=geo_path)

the_map.save("OSM_map.html")

