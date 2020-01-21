"""
Upload a slice of data to your personal wunderground weather station data set
via the rtupdate.wunderground.com interface.

The data provided is generally generated by a personal weather station.

A companion project is available for La Crosse Technology Weather Station owners
at: https://github.com/keithprickett/lacrosse_weather

```
    station_id = 'YOUR STATION ID'
    station_key = 'YOUR STATION KEY'
    weather_data = dict(
        tempf=47.84,
        humidity=94.0
    )
    utc_timestamp = 1579559564
    wunderground_upload_data_point(station_id, station_key, weather_data, utc_timestamp)
```
"""


import requests
import datetime


def wunderground_upload_data_point(station_id, station_key, weather_data, utc_timestamp):
    """ Upload a slice of weather data at a specific UTC timestamp
    Data may include fields listed here:
      https://feedback.weather.com/customer/en/portal/articles/2924682-pws-upload-protocol?b_id=17298
    This function automatically includes the ID, PASSWORD, action, dateutc, realtime, and rtfreq fields
    and the weather_data dict can be used to add additional fields.

    :param station_id: The wunderground station id
    :param station_key: The wunderground station key
    :param weather_data: dictionary of additional fields to include
    :param utc_timestamp: an integer utc timestamp
    """
    payload = {
        'action': 'updateraw',
        'dateutc': timestamp_format(utc_timestamp),
        'ID': station_id,
        'PASSWORD': station_key,
        'realtime': 1,
        'rtfreq': 2.5
    }
    payload.update(weather_data)
    try:
        requests.get('http://rtupdate.wunderground.com/weatherstation/updateweatherstation.php', params=payload)
    except Exception:
        print("Failed to post weather update to wunderground.")


def timestamp_format(utc_timestamp):
    return datetime.datetime.utcfromtimestamp(utc_timestamp).strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    station_id = 'YOUR STATION ID HERE'
    station_key = 'YOUR STATION KEY HERE'
    weather_data = dict(
        tempf=47.84,
        humidity=94.0
    )
    utc_timestamp = 1579559564
    wunderground_upload_data_point(station_id, station_key, weather_data, utc_timestamp)
