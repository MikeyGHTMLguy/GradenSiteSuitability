import geopy
import geopandas
import pandas as pd
import pvlib

from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

geolocator = Nominatim(user_agent="mikey_garden_site_suitability")

address = input("Enter an Address:")
location = geolocator.geocode(address)

if location is None:
    print("Address not found, try again.")
else:
    print("Location Found:" + location.address)
    print("Latitude and Longitude:" + str(location.latitude) + ", " + str(location.longitude))
    print(location.raw)

    tf = TimezoneFinder()
    timezone_str = tf.timezone_at(lat=location.latitude, lng=location.longitude)
    print(timezone_str)

    timeofday = [6, 9, 12, 15, 18]
    months = [3, 4, 5, 6, 7, 8, 9, 10]
    sunlightpoints = [pd.Timestamp(f'2025-{month}-21 {hour}:00:00', tz=timezone_str) for month in months for hour in timeofday]
    print(sunlightpoints)
    
    solar_positions = pvlib.solarposition.get_solarposition(sunlightpoints, location.latitude, location.longitude)
    print(solar_positions[["apparent_elevation", "azimuth"]])

