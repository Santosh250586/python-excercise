import folium
map = folium.Map(location= [28.70, 77.10], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[28.6, 76.5], popup = "Hi I am Marker", icon= folium.Icon(color='orange')))
map.add_child(fg)

map.save("Map1.html")