import ee

class OthersInitialization:
    def __init__(self, m, date_one, date_two):
        self.m = m
        self.date_one = date_one
        self.date_two = date_two

    def firms_init(self):
        firms = ee.ImageCollection("FIRMS").filterDate(str(self.date_one.value), str(self.date_two.value))
        vis_firms = {
            min: 325.0,
            max: 400.0,
        }
        self.m.addLayer(firms, vis_firms, "NASA FIRMS")

    def alostd_init(self):
        alos_td = ee.Image("CSP/ERGo/1_0/Global/ALOS_topoDiversity")
        alos_topodiv = alos_td.select('constant')
        vis_alos_td = {
            min: 0.0,
            max: 1.0,
        }
        self.m.addLayer(alos_topodiv, vis_alos_td, "ALOS TD")
