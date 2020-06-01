import folium
map = folium.Map(location= [38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[38.2, -99.1], [37.3, -98.2]]:
    fg.add_child(folium.Marker(location=coordinates, popup = "Hi I am Marker", icon= folium.Icon(color='orange')))
map.add_child(fg)

map.save("Map3.html")