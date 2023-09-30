import requests

OPEN_WEATHER_MAP_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY = '' ###API KEY GOES HERE (STR)

weather_params = {
    'lat':-19.865010,
    'lon':-43.983825,
    'appid': API_KEY,
}

response = requests.get(OPEN_WEATHER_MAP_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
current_days_forecast = weather_data['list'][:5]
# print(current_days_forecast)

current_days_ids = []

for hour in current_days_forecast:
    weather_id = hour['weather'][0]['id']
    current_days_ids.append(weather_id)
    # print(weather_id)

# print(current_days_ids)

rain_today = False
for id in current_days_ids:
    if id < 700:
        rain_today = True

if rain_today == True:
    print('Gonna rain today bitch')




