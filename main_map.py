import folium
import pandas


df=pandas.read_csv("goa_mf.csv")

map=folium.map(location=[df['Latitude'].mean(),df['Longitude'].mean()],zoom_start=6,tiles='Mapbox bright')

fg=folium.FeatureGroup(name = "Goa Map")

for lat,lon,fac_t,in zip(df['Latitude'],df['Longitude'],df['Facility_Type']):
    fg.add_child(folium.Marker(location=[lat,lon],popup=(folium.popup(fac_t)),icon=folium.Icon(icon_color='green')))

map.add_child(fg)

map.add_child(folium.GeoJson(data=open('india_states.json')))


map.save('map_to.html')