import folium

def additional_datasets(map_folium):
    political_countries_url = (
        "http://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson"
    )

    folium.GeoJson(political_countries_url, name='World Political Map').add_to(map_folium)

def map_layers(map_folium):
    folium.TileLayer('cartodbpositron', name='Bright-colored map').add_to(map_folium)
    folium.TileLayer('cartodbdark_matter', name='Dark-colored map').add_to(map_folium)

def dual_maps_processing(map_folium):
    folium.TileLayer("openstreetmap").add_to(map_folium.m1)
    folium.TileLayer("openstreetmap").add_to(map_folium.m2)
    folium.TileLayer("cartodb dark_matter", name='Dark-colored map').add_to(map_folium.m1)
    folium.TileLayer("cartodb dark_matter", name='Dark-colored map').add_to(map_folium.m2)
    folium.TileLayer('cartodbpositron', name='Bright-colored map').add_to(map_folium.m1)
    folium.TileLayer('cartodbpositron', name='Bright-colored map').add_to(map_folium.m2)
    folium.LayerControl(collapsed=False).add_to(map_folium)
