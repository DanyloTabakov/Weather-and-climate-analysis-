# src/fetch_data.py

from datetime import datetime
from meteostat import Point, Daily

def fetch_decade_data(lat, lon, start_year, end_year):
    """
    Fetch daily weather data for a given location and decade.
    Returns a Pandas DataFrame with daily records.
    """
    location = Point(lat, lon)
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)

    data = Daily(location, start, end).fetch()
    return data
