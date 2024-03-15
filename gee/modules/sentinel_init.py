import ee
import mercury as mr
import txtreading as txtr
import sys

sys.path.insert(0, 'common//') # common files

class SentinelInitialization:
    def __init__(self, m, date_one, date_two, max_cloud_covering):
        self.m = m
        self.date_one = date_one
        self.date_two = date_two
        self.max_cloud_covering = max_cloud_covering

    def sen2msisr_init(self):
        self.sen2msibands = mr.MultiSelect(label="Select Sentinel 2 MSI (TOA/SR) bands",
                                      value=['B2', 'B3', 'B4'],
                                      choices=['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B8A', 'B9', 'B11', 'B12'])

        sen2msi_sr = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED').filterDate(str(self.date_one.value),str(self.date_two.value)).filter(ee.Filter.lte('CLOUDY_PIXEL_PERCENTAGE', self.max_cloud_covering.value))
        composite_sr = sen2msi_sr.median()

        vis_sen2sr = {
            'bands': self.sen2msibands.value,
            'min': txtr.get_min_value('SENTINEL 2 MSI SR'),
            'max': txtr.get_max_value('SENTINEL 2 MSI SR'),
            'gamma': txtr.get_gamma_value('SENTINEL 2 MSI SR'),
        }
        self.m.addLayer(composite_sr, vis_sen2sr, 'Sentinel 2 MSI SR')

    def sen2msitoa_init(self):
        self.sen2msibands = mr.MultiSelect(label="Select Sentinel 2 MSI (TOA/SR) bands",
                                      value=['B2', 'B3', 'B4'],
                                      choices=['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B8A', 'B9', 'B11', 'B12'])

        sen2msi_toa = ee.ImageCollection('COPERNICUS/S2_HARMONIZED').filterDate(str(self.date_one.value), str(self.date_two.value)).filter(ee.Filter.lte('CLOUDY_PIXEL_PERCENTAGE', self.max_cloud_covering.value))
        composite_toa = sen2msi_toa.median()

        vis_sen2toa = {
            'bands': self.sen2msibands.value,
            'min': txtr.get_min_value('SENTINEL 2 MSI TOA'),
            'max': txtr.get_max_value('SENTINEL 2 MSI TOA'),
            'gamma': txtr.get_gamma_value('SENTINEL 2 MSI TOA'),
        }
        self.m.addLayer(composite_toa, vis_sen2toa, 'Sentinel 2 MSI TOA')

    def sen5pc_init(self):
        sen5pc = ee.ImageCollection("COPERNICUS/S5P/OFFL/L3_CLOUD").select('cloud_fraction').filterDate(str(self.date_one.value),str(self.date_two.value))
        vis_sen5pc = {
            min: txtr.get_min_value('SENTINEL 5P CLOUD'),
            max: txtr.get_max_value('SENTINEL 5P CLOUD'),
            'palette': ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']
        }
        self.m.addLayer(sen5pc, vis_sen5pc, 'Sentinel 5P Cloud')
