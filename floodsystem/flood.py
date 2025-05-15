from floodsystem.stationdata import update_water_levels 
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def stations_level_over_threshold(stations, tol):
    stations_otl = []        # initialise empty list
    update_water_levels(stations)   # update water levels to get latest level data for relative_water_level function
    for i in range(len(stations)):
        station = stations[i]
        if station.relative_water_level() == None:   # check for nonetype relative water levels 
            continue 
        if station.relative_water_level() > tol:        # compare water level to tolerance value, this is where nonetype error keeps occuring
            relative_level = station.relative_water_level()
            stations_otl.append((station, relative_level))     # if over tolerance, add to final list
        
    otl_list = sorted(stations_otl, key=lambda t: t[1], reverse = True)   # sort by second entry in tuple
    return otl_list



def stations_highest_rel_level(stations, N):   
    consistent_stations = []     # initialise list
    for i in stations:
        if i.relative_water_level() == None:   # check for nonetype relative water levels 
            continue 
        else: 
            consistent_stations.append(i)

    highest_stations = sorted(consistent_stations, key=lambda x: x.relative_water_level(), reverse=True)   # sort using class method
    top_N_stations = highest_stations[:N] #changed 10 to N

    return top_N_stations




def issue_flood_warnings(stations):
    print("Generating town severities...")
    station_risks = {}
    update_water_levels(stations)
    for i in stations:
        if i.relative_water_level() == None:
            continue
        elif i.relative_water_level() > 0.4:
            station_risks[i] = 3
        elif i.relative_water_level() > 0.15:
            station_risks[i] = 2
            continue
        else:
            station_risks[i] = 1
            continue
        
         # assesing rate of level rising over last day
        previous_level = fetch_measure_levels(i.measure_id, dt=datetime.timedelta(days=1))[1]
        current_level = i.latest_level
        if len(previous_level) > 0:
            change_of_level = (current_level - previous_level[-1])
        else:
            change_of_level = None
        
        if change_of_level == None:
            pass
        elif change_of_level >= 0:
            station_risks[i] += 1

    # severities in towns
    town_severities =  {}
    for j in station_risks.items():
        severity = j[1]
        town = j[0].town
        if town in town_severities:
            if severity >= town_severities[town]:
                town_severities[town] = severity
        else:
            town_severities[town] = severity

    
    for i in town_severities.items():
        if i[1] == 4:
            town_severities[i[0]] = "Severe flood warning"
        elif i[1] == 3:
            town_severities[i[0]] = "High flood warning"
        elif i[1] == 2:                      
            town_severities[i[0]] = "Moderate flood warning"
        else:
            town_severities[i[0]] = "Low flood warning"

    

    return town_severities

        




    