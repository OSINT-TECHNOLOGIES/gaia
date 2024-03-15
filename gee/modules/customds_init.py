import ee
import mercury as mr

def customds_initialization(m):
    custom_ds = mr.Text(value="-", label="[Custom DS] Enter GEE dataset name", rows=1)
    date_one_custom = mr.Text(value="1972-01-01", label="[Custom DS] Enter start date (format YYYY-MM-DD)", rows=1)
    date_two_custom = mr.Text(value="1973-01-01", label="[Custom DS] Enter final date (format YYYY-MM-DD)", rows=1)
    mr.Markdown(text="**CUSTOM DATASETS TIME PERIOD: from {} to {}**".format(date_one_custom.value, date_two_custom.value))
    ds = ee.ImageCollection(custom_ds.value).filterDate(str(date_one_custom.value), str(date_two_custom.value))
    custom_bands = mr.MultiSelect(label="[Custom DS] Select dataset bands",
                                value=[],
                                choices=['SR_B1', 'SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11'])

    ds_custom = ds.select(custom_bands.value)
    vis_custom = {'bands': custom_bands.value}

    m.addLayer(ds_custom, vis_custom, "Custom GEE dataset")
