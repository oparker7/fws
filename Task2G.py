from floodsystem.stationdata import build_station_list as bsl
from floodsystem.stationdata import update_water_levels 
from floodsystem.flood import issue_flood_warnings


def run():
    stations = bsl()
    update_water_levels(stations) 

    for i in issue_flood_warnings(stations[:50]).items():
            print(i)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()