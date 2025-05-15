from floodsystem.stationdata import *
from datetime import *
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
def run():
    """Requirements for Task 2E"""

    stations = build_station_list()
    update_water_levels(stations)
    n = 5
    st_lev = stations_highest_rel_level(stations, n)
    high_sts = []
    for i in range (0,len(st_lev)):
        high_sts.append(st_lev[i])
#high_sts = stations[:n]
#print(type(high_sts[1]))
    #high_sts = [stations[0]]
    dt = 10
    for i in high_sts:
        dates, levels = fetch_measure_levels(i.measure_id, dt=timedelta(days=dt)) #measure_id
        plot_dates = []
        plot_levels = []
        for date, level in zip(dates, levels):
            plot_dates.append(date)
            plot_levels.append(level)
        plot_water_levels(i, plot_dates, plot_levels)



if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()