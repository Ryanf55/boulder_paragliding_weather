import pysmartweatherudp as psw

import logging


def heading_to_cardinal(d):
    dirs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    ix = round(d / (360. / len(dirs)))
    return dirs[ix % len(dirs)]

meas = {}

def data_callback(df):
    if type(df) == psw.utils.RapidWind:
        speed = df.wind_speed_rapid
        heading = df.wind_bearing_rapid     # (degrees CW from true north)
        gust = df.wind_gust
        print(int(heading))
        print(heading_to_cardinal(int(heading)))

    elif type(df) == psw.utils.SkyObservation:
        pass
    elif type(df) == psw.utils.AirObservation:
        pass
    # elif type(df) == psw.utils.StObservation:
    #     pass
    else:
        print("Unknown data callback type of %s", type(df))


if __name__ == "__main__":
    swr = psw.SWReceiver() # Using default host, port, units
    swr.registerCallback(data_callback)
    try:
        swr.run()
        print("Running")
    except KeyboardInterrupt:
        swr.stop()
