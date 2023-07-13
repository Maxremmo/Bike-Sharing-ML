import pandas as pd
import requests
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point, Polygon

base_url = 'https://gbfs.capitalbikeshare.com/gbfs/gbfs.json'

def main_request(url):

    r = requests.get(base_url)
    data = r.json()

    return data


def station_info(data):
    
    r = requests.get(data['data']['en']['feeds'][1]['url'])
    station_info = r.json()

    return station_info


def parse_station_info(stations_json):

    station_list = []
    last_update = stations_json['last_updated']
    for station in range(len(stations_json['data']['stations'])):
        region_id = stations_json['data']['stations'][station]['region_id']
        has_kiosk = stations_json['data']['stations'][station]['has_kiosk']
        station_type = stations_json['data']['stations'][station]['station_type']
        adress = stations_json['data']['stations'][station]['name']
        capacity = stations_json['data']['stations'][station]['capacity']
        latitude = stations_json['data']['stations'][station]['lat']
        longitude = stations_json['data']['stations'][station]['lon']
        rental_methods = stations_json['data']['stations'][station]['rental_methods']
        station_id = stations_json['data']['stations'][station]['station_id']
        legacy_id = stations_json['data']['stations'][station]['legacy_id']

        station_dict = {
            'region_id' : region_id,
            'adress' : adress,
            'latitude': latitude,
            'longitude' : longitude,
            'type' : station_type,
            'has_kiosk' : has_kiosk,
            'capacity' : capacity,
            'rental_methods' : rental_methods,
            'station_id' : station_id,
            'legacy_id' : legacy_id,
            'last_updated' : dt.datetime.fromtimestamp(last_update)
        }

        station_list.append(station_dict)
        
    return station_list   


def get_bike_info(data):
    
    resp = requests.get(data['data']['en']['feeds'][3]['url'])
    bike_data = resp.json()

    return bike_data

def parse_bike_info(bike_json):
    bike_list = []
    last_update = bike_json['last_updated']
    for bike in range(len(bike_json['data']['bikes'])):
        bike_id = bike_json['data']['bikes'][bike]['bike_id']
        latitude = bike_json['data']['bikes'][bike]['lat']
        longitude = bike_json['data']['bikes'][bike]['lon']
        longitude = bike_json['data']['bikes'][bike]['lon']
        type = bike_json['data']['bikes'][bike]['type']
        reserved = bike_json['data']['bikes'][bike]['is_reserved']
        disabled = bike_json['data']['bikes'][bike]['is_disabled']
        bike_dict = {
            'bike_id' : bike_id,
            'latitude': latitude,
            'longitude' : longitude,
            'bike_type' : type,
            'reserved' : reserved,
            'disabled' : disabled,
            'last_updated' : dt.datetime.fromtimestamp(last_update)
        }
        bike_list.append(bike_dict)
    return bike_list

df_stations = pd.DataFrame(parse_station_info(station_info(main_request(base_url))))
df_bikes = pd.DataFrame(parse_bike_info(get_bike_info(main_request(base_url))))

geometry = [Point(xy) for xy in zip(df_stations['longitude'], df_stations['latitude'])]
crs = {'init':'epsg:3395'}

geo_df = gpd.GeoDataFrame(df_stations,
                          crs=crs,
                          geometry=geometry)

washington = gpd.read_file('datasets/tl_2018_11001_roads/tl_2018_11001_roads.shp')

fig, ax = plt.subplots(figsize=(12, 12))
# Plot the Washington, D.C. map
washington.plot(ax=ax, zorder= 1)
# Plot the GeoDataFrame on the axis
geo_df.plot(ax=ax, marker='o', color='red', markersize=5, zorder=2)
# Set the plot extent to Washington, D.C.
ax.set_xlim(washington.total_bounds[0], washington.total_bounds[2])
ax.set_ylim(washington.total_bounds[1], washington.total_bounds[3])
# Customize the map appearance (optional)
ax.set_title("Bike-sharing stations in Washington, D.C.")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

# Display the map
plt.show()

geometry = [Point(xy) for xy in zip(df_bikes['longitude'], df_bikes['latitude'])]

geo_df = gpd.GeoDataFrame(df_bikes,
                          crs=crs,
                          geometry=geometry)

fig, ax = plt.subplots(figsize=(12, 12))
# Plot the Washington, D.C. map
washington.plot(ax=ax, zorder= 1)

# Plot the GeoDataFrame on the axis
geo_df.plot(ax=ax, marker='o', color='red', markersize=5, zorder=2)

# Set the plot extent to Washington, D.C.
ax.set_xlim(washington.total_bounds[0], washington.total_bounds[2])
ax.set_ylim(washington.total_bounds[1], washington.total_bounds[3])

# Customize the map appearance (optional)
ax.set_title("Available Bikes in Washington, D.C.")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

# Display the map
plt.show()