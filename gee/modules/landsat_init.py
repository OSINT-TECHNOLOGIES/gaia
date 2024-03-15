import ee
import mercury as mr
import txtreading as txtr
import sys

sys.path.insert(0, 'common//') # common files

class LandsatInitialization:
    def __init__(self, m, date_one, date_two, max_cloud_covering):
        self.m = m
        self.date_one = date_one
        self.date_two = date_two
        self.max_cloud_covering = max_cloud_covering

    def ls7sr_init(self):
        self.ls7bands = mr.MultiSelect(label="Select LandSat 7 SR bands",
                                  value=['SR_B3', 'SR_B2', 'SR_B1'],
                                  choices=['SR_B1', 'SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'])
        ls7 = ee.ImageCollection("LANDSAT/LE07/C02/T1_L2").filterDate(str(self.date_one.value), str(self.date_two.value)).filter(
            ee.Filter.lte('CLOUD_COVER', self.max_cloud_covering.value))
        vis_ls7 = {'bands': self.ls7bands.value}
        self.m.addLayer(ls7, vis_ls7, "LandSat 7 SR", True, 0.7)

    def ls8toa_init(self):
        self.ls8bands = mr.MultiSelect(label="Select LandSat 8 TOA/RAW bands",
                                  value=['B4', 'B3', 'B2'],
                                  choices=['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11'])
        ls8 = ee.ImageCollection("LANDSAT/LC08/C02/T1_TOA").filterDate(str(self.date_one.value), str(self.date_two.value)).filter(
            ee.Filter.lte('CLOUD_COVER', self.max_cloud_covering.value))
        vis_ls8 = {
            'bands': self.ls8bands.value,
            'min': txtr.get_min_value('LANDSAT 8 TOA'),
            'max': txtr.get_max_value('LANDSAT 8 TOA'),
        }
        self.m.addLayer(ls8, vis_ls8, 'LandSat 8 TOA')

    def ls8rawtc_init(self):
        self.ls8bands = mr.MultiSelect(label="Select LandSat 8 TOA/RAW bands",
                                  value=['B4', 'B3', 'B2'],
                                  choices=['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11'])
        ls8raw = ee.ImageCollection('LANDSAT/LC09/C02/T1').filterDate(str(self.date_one.value), str(self.date_two.value)).filter(
            ee.Filter.lte('CLOUD_COVER', self.max_cloud_covering.value))
        ls8raw_tc = ls8raw.select(self.ls8bands.value)
        vis_ls8raw_tc = {
            min: txtr.get_min_value('LANDSAT 8 RAW'),
            max: txtr.get_max_value('LANDSAT 8 RAW'),
        }
        self.m.addLayer(ls8raw_tc, vis_ls8raw_tc, "LandSat 8 RAW")

    def ls8sr_init(self):
        self.ls8srbands = mr.MultiSelect(label="Select LandSat 8 SR bands",
                                    value=['SR_B4', 'SR_B3', 'SR_B2'],
                                    choices=['SR_B1', 'SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'])

        ls8sr = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2').filterDate(str(self.date_one.value),
                                                                        str(self.date_two.value)).filter(
            ee.Filter.lte('CLOUD_COVER', self.max_cloud_covering.value))
        vis_ls8sr = {
            'bands': self.ls8srbands.value,
            min: txtr.get_min_value('LANDSAT 8 SR'),
            max: txtr.get_max_value('LANDSAT 8 SR'),
        }
        self.m.addLayer(ls8sr, vis_ls8sr, 'LandSat 8 SR')

    def ls9_init(self):
        self.ls9bands = mr.MultiSelect(label="Select LandSat 9 SR bands",
                                  value=['SR_B4', 'SR_B3', 'SR_B2'],
                                  choices=['SR_B1', 'SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'])
        def apply_scale_factors(image):
            opticalBands = image.select('SR_B.').multiply(0.0000275).add(-0.2)
            thermalBands = image.select('ST_B.*').multiply(0.00341802).add(149.0)
            return image.addBands(opticalBands, None, True).addBands(thermalBands, None, True)

        collection = ee.ImageCollection('LANDSAT/LC09/C02/T1_L2').filterDate(str(self.date_one.value),
                                                                             str(self.date_two.value)).filter(
            ee.Filter.lte('CLOUD_COVER', self.max_cloud_covering.value))

        median = collection.median()
        ls9 = apply_scale_factors(median)

        vis_ls9 = {
            'bands': self.ls9bands.value,
            'min': txtr.get_min_value('LANDSAT 9 SR'),
            'max': txtr.get_max_value('LANDSAT 9 SR'),
        }
        self.m.addLayer(ls9, vis_ls9, 'LandSat 9 SR')


    def ls9rawtc_init(self):
        self.ls9rawbands = mr.MultiSelect(label="Select LandSat 9 RAW/TOA bands",
                                     value=['B4', 'B3', 'B2'],
                                     choices=['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11'])
        ls9raw = ee.ImageCollection("LANDSAT/LC09/C02/T2").filterDate(str(self.date_one.value), str(self.date_two.value)).filter(
            ee.Filter.lte('CLOUD_COVER', self.max_cloud_covering.value))
        ls9raw_tc = ls9raw.select(self.ls9rawbands.value)
        vis_ls9raw_tc = {
            'min': txtr.get_min_value('LANDSAT 9 RAW'),
            'max': txtr.get_max_value('LANDSAT 9 RAW'),
        }
        self.m.addLayer(ls9raw_tc, vis_ls9raw_tc, 'LandSat 9 RAW')

    def ls9toatc_init(self):
        self.ls9rawbands = mr.MultiSelect(label="Select LandSat 9 RAW/TOA bands",
                                     value=['B4', 'B3', 'B2'],
                                     choices=['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11'])
        ls9toa = ee.ImageCollection('LANDSAT/LC09/C02/T1_TOA').filterDate(str(self.date_one.value),
                                                                          str(self.date_two.value)).filter(
            ee.Filter.lte('CLOUD_COVER', self.max_cloud_covering.value))
        ls9toa_tc = ls9toa.select(self.ls9rawbands.value)
        vis_ls9toa_tc = {
            min: txtr.get_min_value('LANDSAT 9 TOA'),
            max: txtr.get_max_value('LANDSAT 9 TOA'),
        }
        self.m.addLayer(ls9toa_tc, vis_ls9toa_tc, 'LandSat 9 TOA')
