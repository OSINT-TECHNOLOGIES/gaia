import ee
import mercury as mr

def landsat_initialization(m, date_one, date_two, max_cloud_covering):
    ls7bands = mr.MultiSelect(label="Select LandSat 7 SR bands",
                              value=['SR_B3', 'SR_B2', 'SR_B1'],
                              choices=['SR_B1', 'SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'])

    ls8bands = mr.MultiSelect(label="Select LandSat 8 TOA/RAW bands",
                              value=['B4', 'B3', 'B2'],
                              choices=['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11'])

    ls8srbands = mr.MultiSelect(label="Select LandSat 8 SR bands",
                                value=['SR_B4', 'SR_B3', 'SR_B2'],
                                choices=['SR_B1', 'SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'])

    ls9bands = mr.MultiSelect(label="Select LandSat 9 SR bands",
                              value=['SR_B4', 'SR_B3', 'SR_B2'],
                              choices=['SR_B1', 'SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'])

    ls9rawbands = mr.MultiSelect(label="Select LandSat 9 RAW/TOA bands",
                                 value=['B4', 'B3', 'B2'],
                                 choices=['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11'])

    #LANDSAT 7
    ls7 = ee.ImageCollection("LANDSAT/LE07/C02/T1_L2").filterDate(str(date_one.value), str(date_two.value)).filter(ee.Filter.lte('CLOUD_COVER', max_cloud_covering.value))
    vis_ls7 = {'bands': ls7bands.value}

    #LANDSAT 8 TOA
    ls8 = ee.ImageCollection("LANDSAT/LC08/C02/T1_TOA").filterDate(str(date_one.value), str(date_two.value)).filter(ee.Filter.lte('CLOUD_COVER', max_cloud_covering.value))
    vis_ls8 = {
        'bands': ls8bands.value,
        'min': 0.0,
        'max': 0.4,
    }

    #LANDSAT 8 RAW
    ls8raw = ee.ImageCollection('LANDSAT/LC09/C02/T1').filterDate(str(date_one.value), str(date_two.value)).filter(ee.Filter.lte('CLOUD_COVER', max_cloud_covering.value))
    ls8raw_tc = ls8raw.select(ls8bands.value)
    vis_ls8raw_tc = {
        min: 0.0,
        max: 30000.0,
    }

    #LANDSAT 8 SR
    ls8sr = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2').filterDate(str(date_one.value), str(date_two.value)).filter(ee.Filter.lte('CLOUD_COVER', max_cloud_covering.value))
    vis_ls8sr = {
        'bands': ls8srbands.value,
        min: 0.0,
        max: 0.3,
    }

    #LANDSAT 9
    def apply_scale_factors(image):
        opticalBands = image.select('SR_B.').multiply(0.0000275).add(-0.2)
        thermalBands = image.select('ST_B.*').multiply(0.00341802).add(149.0)
        return image.addBands(opticalBands, None, True).addBands(thermalBands, None, True)

    collection = ee.ImageCollection('LANDSAT/LC09/C02/T1_L2').filterDate(str(date_one.value), str(date_two.value)).filter(ee.Filter.lte('CLOUD_COVER', max_cloud_covering.value))
    median = collection.median()
    ls9 = apply_scale_factors(median)

    vis_ls9 = {
        'bands': ls9bands.value,
        'min': 0.0,
        'max': 0.3,
    }

    #LANDSAT 9 RAW
    ls9raw = ee.ImageCollection("LANDSAT/LC09/C02/T2").filterDate(str(date_one.value), str(date_two.value)).filter(ee.Filter.lte('CLOUD_COVER', max_cloud_covering.value))
    ls9raw_tc = ls9raw.select(ls9rawbands.value)
    vis_ls9raw_tc = {
        'min': 0.0,
        'max': 30000.0,
    }

    #LANDSAT 9 TOA
    ls9toa = ee.ImageCollection('LANDSAT/LC09/C02/T1_TOA').filterDate(str(date_one.value), str(date_two.value)).filter(ee.Filter.lte('CLOUD_COVER', max_cloud_covering.value))
    ls9toa_tc = ls9toa.select(ls9rawbands.value)
    vis_ls9toa_tc = {
        min: 0.0,
        max: 0.4,
    }

    m.addLayer(ls7, vis_ls7, "LandSat 7 SR", True, 0.7)
    m.addLayer(ls8, vis_ls8, 'LandSat 8 TOA')
    m.addLayer(ls8raw_tc, vis_ls8raw_tc, "LandSat 8 RAW")
    m.addLayer(ls8sr, vis_ls8sr, 'LandSat 8 SR')
    m.addLayer(ls9, vis_ls9, 'LandSat 9 SR')
    m.addLayer(ls9raw_tc, vis_ls9raw_tc, 'LandSat 9 RAW')
    m.addLayer(ls9toa_tc, vis_ls9toa_tc, 'LandSat 9 TOA')