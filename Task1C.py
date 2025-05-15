from floodsystem.stationdata import build_station_list as bsl
from floodsystem.geo import stations_within_radius as swr

def run():

    nearby_station_objects = swr(bsl(), (52.2053, 0.1218), 10)
    nearby_stations = []

    for i in nearby_station_objects:
        nearby_stations.append(i.name)

    nearby_stations.sort()
    print(nearby_stations)


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
