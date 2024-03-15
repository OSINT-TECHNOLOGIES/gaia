import ee
import txtreading as txtr
import sys

sys.path.insert(0, 'common//') # common files

class OthersInitialization:
    def __init__(self, m, date_one, date_two):
        self.m = m
        self.date_one = date_one
        self.date_two = date_two

    def firms_init(self):
        firms = ee.ImageCollection("FIRMS").filterDate(str(self.date_one.value), str(self.date_two.value))
        vis_firms = {
            min: txtr.get_min_value('NASA FIRMS'),
            max: txtr.get_max_value('NASA FIRMS'),
        }
        self.m.addLayer(firms, vis_firms, "NASA FIRMS")

    def alostd_init(self):
        alos_td = ee.Image("CSP/ERGo/1_0/Global/ALOS_topoDiversity")
        alos_topodiv = alos_td.select('constant')
        vis_alos_td = {
            min: txtr.get_min_value('ALOS TD'),
            max: txtr.get_max_value('ALOS TD'),
        }
        self.m.addLayer(alos_topodiv, vis_alos_td, "ALOS TD")
