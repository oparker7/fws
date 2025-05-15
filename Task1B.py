from floodsystem.stationdata import build_station_list as bsl
from floodsystem.geo import stations_by_distance as sbd

def run():

    station_objects_distanced = sbd(bsl(), (52.2053, 0.1218))
    station_tuples_distanced = []

    for station in station_objects_distanced:
        current_station = ((station[0]).name, (station[0]).town, station[1])
        station_tuples_distanced.append(current_station)

    closest_stations = station_tuples_distanced[:10]
    furthest_stations = station_tuples_distanced[-10:]

    print('The ten stations closest to Cambridge City Centre are: ')
    for i in closest_stations:
        print(i)

    print('The ten stations furthest from Cambridge City Centre are: ')
    for i in furthest_stations:
        print(i)

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run() 