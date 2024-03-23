from folium import plugins
from folium.plugins import Draw

def geocoder_init(m):
    plugins.Geocoder(
        position='bottomleft',
        force_separate_button=True
    ).add_to(m)

def draw_init(m):
    draw = Draw(export=True)
    draw.add_to(m)

def minimap_init(m):
    plugins.MiniMap().add_to(m)

def terminator_init(m):
    plugins.Terminator().add_to(m)

def basemaps_init(m):
    m.add_basemap('HYBRID')
    m.add_basemap('TERRAIN') 

def additional_basemaps_init(m):
    m.add_basemap('ESRI')
    m.add_basemap('Esri Ocean')
    m.add_basemap('Esri Terrain')
    m.add_basemap('Esri Transportation')
    m.add_basemap('Esri Topo World')
    m.add_basemap('Esri National Geographic')
    m.add_basemap('Esri Shaded Relief')