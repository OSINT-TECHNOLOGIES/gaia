import ee

class ModisInitialization:
    def __init__(self, m, date_one, date_two, max_cloud_covering):
        self.m = m
        self.date_one = date_one
        self.date_two = date_two
        self.max_cloud_covering = max_cloud_covering

    def modissc_init(self):
        modis_sc = ee.ImageCollection('MODIS/061/MOD10A1').filterDate(str(self.date_one.value), str(self.date_two.value))
        modis_snowcover = modis_sc.select('NDSI_Snow_Cover')
        vis_modis_sc = {
            min: 0.0,
            max: 100.0,
            'palette': ['black', '0dffff', '0524ff', 'ffffff'],
        }
        self.m.addLayer(modis_snowcover, vis_modis_sc, "MODIS Snowcover", True, 0.7)

    def modistsr_init(self):
        modis_tsr = ee.ImageCollection('MODIS/061/MOD09GQ').filterDate(str(self.date_one.value), str(self.date_two.value))
        vis_modis_tsr = {
            min: -100.0,
            max: 8000.0,
            'bands': ['sur_refl_b02', 'sur_refl_b02', 'sur_refl_b01']
        }
        self.m.addLayer(modis_tsr, vis_modis_tsr, 'MODIS TSR')

    def modistta_init(self):
        modis_tta = ee.ImageCollection('MODIS/061/MOD14A1').filterDate(str(self.date_one.value), str(self.date_two.value))
        vis_modis_tta = {
            min: 0.0,
            max: 6000.0,
            'bands': ['MaxFRP', 'FireMask', 'FireMask'],
        }
        self.m.addLayer(modis_tta, vis_modis_tta, "MODIS TTA&FD")
