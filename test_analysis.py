from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import *
from datetime import datetime, timedelta
import numpy as np
def test_polyfit():
    stations = build_station_list()
    test_dates, test_levels = fetch_measure_levels(stations[0].measure_id, dt=timedelta(days=1))
    poly, axis_shift = polyfit(test_dates, test_levels, 3)
    assert(type(poly)==np.poly1d)
    assert(type(axis_shift)==np.float64 and axis_shift != 0) #check the shift value is the correct type and there is a shift