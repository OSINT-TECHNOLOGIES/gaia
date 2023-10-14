import ee

def others_initialization(m, date_one, date_two):
    firms = ee.ImageCollection("FIRMS").filterDate(str(date_one.value), str(date_two.value))
    vis_firms = {
        min: 325.0,
        max: 400.0,
    }

    alos_td = ee.Image("CSP/ERGo/1_0/Global/ALOS_topoDiversity")
    alos_topodiv = alos_td.select('constant')
    vis_alos_td = {
        min: 0.0,
        max: 1.0,
    }

    m.addLayer(firms, vis_firms, "NASA FIRMS")
    m.addLayer(alos_topodiv, vis_alos_td, "ALOS TD")
