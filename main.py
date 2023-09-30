import requests

OPEN_WEATHER_MAP_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'
API_KEY = pass ###API KEY INSIDE A STRING GOES HERE

weather_params = {
    'lat': -19.865008,
    'long': -43.984186,
    'appid': API_KEY,
    'exclude': 'current,minutely,daily',
}

response = requests.get(OPEN_WEATHER_MAP_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
cunrrent_weather_id = weather_data['hourly'][0]['weather'][0]['id']
