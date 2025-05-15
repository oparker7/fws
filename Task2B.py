from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels 

def run():
        stations = build_station_list() # builds list of MonitoringStation objects
        update_water_levels(stations)

        stations_at_risk = stations_level_over_threshold(stations, 0.8) # Finds a list of stations where the relative risk level over 0.8
        for i in stations_at_risk: 
                print((i[0]).name, i[1])


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()