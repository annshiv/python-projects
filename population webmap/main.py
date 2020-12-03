# import modules
import folium
import pandas

# exact data and divided into variable name
data = pandas.read_csv("volcanoes.txt")
lat = data["LAT"]
lon = data["LON"]
name = data["Name"]
loc = data["Location"]

# world map started in india
map = folium.Map(location = [23.11415676940592, 78.55842774063291],zoom_start = 5,tiles="Stamen Terrain")

# volcanes markers in india
for n,l,lt , ln in zip(name,loc,lat,lon):
    iframe = folium.IFrame(n+", "+l, width=200, height=70)
    map.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(iframe), icon = folium.Icon(color="red")))

# poluation colors add
map.add_child(folium.GeoJson(data=open('world.json','r',encoding="utf-8-sig").read(),style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] <10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# save as html 
map.save("map.html")