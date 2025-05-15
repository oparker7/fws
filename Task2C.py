from floodsystem.stationdata import build_station_list as bsl
from floodsystem.stationdata import update_water_levels 
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = bsl() # builds list of MonitoringStation objects
    update_water_levels(stations)

    stations_with_highest_level = stations_highest_rel_level(stations, 10)
    for i in stations_with_highest_level:
        print(i.name, i.relative_water_level())

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()