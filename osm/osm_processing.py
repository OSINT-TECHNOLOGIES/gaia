import matplotlib.pyplot as plt
import osmnx as ox
import contextily as cx
import folium

def map_plotting(map_size, place_long, place_lat, place_delta):
    west, south, east, north = (float(place_long), float(place_lat) - float(place_delta), float(place_long) + float(place_delta), float(place_lat))
    im, bbox = cx.bounds2img(west, south, east, north, ll=True, source=cx.providers.OpenStreetMap.Mapnik)
    plt.figure(figsize=(map_size.value, map_size.value))
    plt.imshow(im)
    plt.show()

def sn_analysis(place_long, place_lat):
    G = ox.graph_from_point((float(place_lat), float(place_long)), dist=100000, network_type='drive')
    ox.plot_graph(G)

def building_analysis(place_long, place_lat):
    gdf = ox.features_from_point((float(place_lat), float(place_long)), tags={'building': True})
    gdf.plot()

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
